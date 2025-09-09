from elasticsearch import Elasticsearch

class UpdateElastic:
    def __init__(self,index):
        self.es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])
        self.index = index

    def update_doc(self, document, id=None, query=None):
        if not id and not query:
            raise ValueError('Needs or id or query')
        elif id and query:
            raise ValueError('Only 1 or id or query')
        elif id and not query:
            self.es.update(index=self.index, id=id, body={'doc': document})
        else:
            self.es.update_by_query(index=self.index, body={'query': query, 'doc': document})

    def get_file_path(self,id):
        return self.es.get(index=self.index,id=id)['_source']['File_Path']



