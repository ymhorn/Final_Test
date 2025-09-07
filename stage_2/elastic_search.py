from elasticsearch import Elasticsearch

class ElasticSearch:
    def __init__(self):
        self.es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])

    def create_index(self,name,mapping = None):
        if not self.es.indices.exists(index=name):
            if mapping:
                self.es.indices.create(index=name, body=mapping)
            else:
                self.es.indices.create(index=name)

    def create_doc(self,document,index,id = None):
        if id:
            self.es.index(index=index,body=document,id=id)
        else:
            self.es.index(index=index, body=document)