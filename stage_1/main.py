from path_object import PathObject
from json_info import JsonBuilder
from kafka_publisher import Produce
from pathlib import Path

main_path = Path(r"C:\Users\Yisroel Meir\Desktop\podcasts")
kafka = Produce()

for file in main_path.iterdir():
    file_object = PathObject(file)
    json_builder = JsonBuilder(file_object)
    kafka.publish_message('meta_data',json_builder.json())


kafka.producer.flush()