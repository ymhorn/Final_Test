from elasticsearch.helpers import scan
from elastic import UpdateElastic
from stt import SpeechToText

update_es = UpdateElastic('meta_data')

stt = SpeechToText()

for doc in scan(update_es.es, index=update_es.index, query={"query": {"match_all": {}}}):
    id = doc['_id']
    file_path = update_es.get_file_path(id)
    text = stt.convert_from_path(file_path)
    update_es.update_doc(document={'audio_text': text},id=id)
