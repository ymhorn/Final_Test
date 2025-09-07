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

class Subscriber:
    def __init__(self,topic):
        self.consumer = KafkaConsumer(topic,
            value_deserializer=lambda m: json.loads(m.decode('ascii')),
            bootstrap_servers=["localhost:9092"])


a = Subscriber('meta_data')
for message in a.consumer:
    print(message.value)