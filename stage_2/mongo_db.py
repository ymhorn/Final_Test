import pymongo
from gridfs import GridFS

class Mongo:
    def __init__(self,database,collection):
        self.mongodb = pymongo.MongoClient("mongodb://mongo:27017")
        self.db = self.mongodb[database]
        self.collection = collection

    def add_audio(self,file_path,file_name,id):
        fs = GridFS(database=self.db,collection=self.collection)
        with open(file_path,'rb') as audio_file:
            fs.put(_id=id,data=audio_file,filename=file_name)
