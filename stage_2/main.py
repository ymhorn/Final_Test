from stage_2.id_creater import IdCreate
from stage_2.kafka_subscriber import Subscriber
from stage_2.elastic_search import ElasticSearch
from stage_2.mongo_db import Mongo
from stage_log.logging_file import Logger
import os

logger = Logger.get_logger()

try:
    topic = os.getenv('TOPIC',default='meta_data')
    mongo_db = os.getenv('MONGO_DB',default='audio')
    mongo_col = os.getenv('MONGO_COL',default='final_test')
    es_index = os.getenv('ES_INDEX',default='meta_data')

    subscriber = Subscriber(topic)
    logger.info(f'Connected to kafka subscriber for topic {topic}')

    es = ElasticSearch()
    logger.info('Created instance of elastic search')

    mongo = Mongo(mongo_db,mongo_col)
    logger.info(f'Connected to mongo: db: {mongo_db}, collection: {mongo_col}')

    es.create_index(es_index)
    logger.info(f'created index {es_index} in elastic search')

    for message in subscriber.consumer:
        path = message.value['File_Path']
        name = message.value['File_Name']

        unique_id = IdCreate.create_unique_id(path)
        logger.info(f'Created unique id for file {name}')

        es.create_doc(document=message.value,index=es_index,id=unique_id)
        logger.info(f'Added document with id: {unique_id} to index: {es_index}')

        mongo.add_audio(file_path=path,file_name=name,id=unique_id)
        logger.info(f'Added the audio of file {name} to mongoDB with id: {unique_id}')

except Exception as e:
    logger.error(f'Did not work, error is: {e}')