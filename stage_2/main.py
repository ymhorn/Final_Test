from id_creater import IdCreate
from kafka_subscriber import Subscriber
from elastic_search import ElasticSearch
from mongo_db import Mongo

subscriber = Subscriber('meta_data')
es = ElasticSearch()
mongo = Mongo('audio','final_test')

es.create_index('meta_data')
for message in subscriber.consumer:
    unique_id = IdCreate.create_unique_id(message.value['File_Path'])
    print(message)
    es.create_doc(document=message.value,index='meta_data',id=unique_id)
    mongo.add_audio(file_path=message.value['File_Path'],file_name=message.value['File_Name'],id=unique_id)
