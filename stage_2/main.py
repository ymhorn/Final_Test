from id_creater import IdCreate
from kafka_subscriber import Subscriber
from elastic_search import ElasticSearch

subscriber = Subscriber('meta_data')
es = ElasticSearch()

es.create_index('meta_data')
for message in subscriber.consumer:
    es.create_doc(document=message.value,index='meta_data',id=IdCreate.create_unique_id(message.value['File_Path']))


