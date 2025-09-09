
from pathlib import Path
import os
from datetime import datetime
from kafka import KafkaConsumer
import json
#
# path = Path(r"C:\Users\Yisroel Meir\Desktop\podcasts")
#
# def time_converter(original_time_format):
#   time = datetime.fromtimestamp(original_time_format)
#   return time
#
# for file in path.iterdir():
#     a = Path(file)
#     c = time_converter(os.path.getctime(a))
#     d = time_converter(os.path.getmtime(a))
#     b ={
#         'file_name': a.stem,
#         'file_path': a,
#         'file_size': os.stat(a).st_size,
#         'file_created':c,
#         'file_last_modified':d,
#     }
#     print(b)
#     # print(time_converter(os.path.getctime(a)))

# class Subscriber:
#     def __init__(self,topic):
#         self.consumer = KafkaConsumer(topic,
#             value_deserializer=lambda m: json.loads(m.decode('ascii')),
#             bootstrap_servers=["localhost:9092"])
#
#
# a = Subscriber('meta_data')
# for message in a.consumer:
#     print(message)

# import checksumdir
# a = checksumdir.dirhash(r"C:\Users\Yisroel Meir\Desktop\podcasts")
# print(a)

# from dirhash import dirhash
#
# a = dirhash(r"C:\Users\Yisroel Meir\Desktop\podcasts\download (4).wav","sha256")
# print(a)

# import hashlib
#
# with open(r"C:\Users\Yisroel Meir\Desktop\podcasts\download (4).wav", "rb") as file:
#     digest = hashlib.file_digest(file , "sha256")
#
# print(digest.hexdigest())


# from pymongo import MongoClient
# from gridfs import GridFS
#
# client = MongoClient('mongodb://localhost:27017/')
# db = client['trial']
# fs = GridFS(db)
#
# with open(r"C:\Users\Yisroel Meir\Desktop\podcasts\download (1).wav", 'rb') as audio_file:
#     file_id = fs.put(audio_file, filename='audio.mp3', content_type='audio/mpeg')
# print(f"Audio file stored with ID: {file_id}")
#
# import logging
# from elasticsearch import Elasticsearch
# from datetime import datetime
# class Logger:
#     _logger = None
#     @classmethod
#     def get_logger(cls, name="meta_data_logging", es_host='http://localhost:9200',
# index="trial", level=logging.DEBUG):
#         if cls._logger:
#             return cls._logger
#         logger = logging.getLogger(name)
#         logger.setLevel(level)
#         if not logger.handlers:
#             es = Elasticsearch(es_host)
#             class ESHandler(logging.Handler):
#                 def emit(self, record):
#                     try:
#                         es.index(index=index, document={
#                             "timestamp": datetime.utcnow().isoformat(),
#                             "level": record.levelname,
#                             "logger": record.name,
#                             "message": record.getMessage()
#                         })
#                     except Exception as e:
#                         print(f"ES log failed: {e}")
#             logger.addHandler(ESHandler())
#             logger.addHandler(logging.StreamHandler())
#         cls._logger = logger
#         return logger
import base64
worse_coded_string = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
less_bad = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="
a = base64.b64decode(worse_coded_string).decode('UTF-8')
b = a.split(',')
c = base64.b64decode(less_bad).decode('UTF-8')
d = c.split(',')
print(b)
print(d)
e = "too many massacres too many families lost and yet it feels like the world forgets within days names faces and homes erased almost as if they never existed that's why memory is essential recording these events telling the stories and refusing to let silence cover them up is a form of resistance every story preserved is a tribute to those who suffered resistance isn't always visible it can be writing teaching children or preserving cultural practices these acts ensure that massacres are not just statistics they are remembered as human tragedies and liberation requires memory without acknowledging the full extent of these atrocities how can justice or piece ever be achieved every protest every report every conversation adds a layer of accountability it's signals that the world is watching and that these families are not alone that's the power of documentation and solidarity even small ripples like podcasts can contribute to a global wave of awareness and sharing that massacres are neither forgotten nor repeated"
amount = len(e.split(' '))
f = amount/33
g = 0
for word in b:
    if word.lower() in e:
        g += 2
for word in d:
    if word.lower() in e:
        g += 1
k = (f/g) * 100
print(k)