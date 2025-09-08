from path_object import PathObject
from json_info import JsonBuilder
from kafka_publisher import Produce
from pathlib import Path
from stage_log.logging_file import Logger
import os

logger = Logger.get_logger()

try:
    path = os.getenv('PARENT_PATH',default=r"C:\Users\Yisroel Meir\Desktop\podcasts")
    topic = os.getenv('TOPIC',default='meta_data')

    main_path = Path(path)
    logger.info(f'Created Path object for directory {main_path.name}')
    kafka = Produce()
    logger.info('Connected to kafka')

    for file in main_path.iterdir():
        file_object = PathObject(file)
        logger.info(f'Created Path object for file {file_object.file_name()}')
        json_builder = JsonBuilder(file_object)
        logger.info(f'All info put into json form for file {file_object.file_name()}')
        kafka.publish_message(topic,json_builder.json())
        logger.info(f'Published json of file {file_object.file_name()} to kafka with topic {topic}')

    kafka.producer.flush()
    logger.info('Kafka publisher finished')

except Exception as e:
    logger.error(f'Did not work, error is: {e}')

