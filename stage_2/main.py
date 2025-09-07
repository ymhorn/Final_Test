from id_creater import IdCreate
from kafka_subscriber import Subscriber
from elastic_search import ElasticSearch
import json

subscriber = Subscriber('meta_data')
es = ElasticSearch()

es.create_index('meta_data')
for message in subscriber.consumer:
    value = message.value.replace("\'", "\"")
    # print(value)
    doc = json.loads(value)
    es.create_doc(document=doc,index='meta_data',id=IdCreate.create_unique_id(doc['File_Path']))


