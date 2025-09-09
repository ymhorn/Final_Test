from elasticsearch.helpers import scan
from elastic import UpdateElastic
from stt import SpeechToText
import os
from stage_log.logging_file import Logger

logger = Logger.get_logger()

try:
    es_index = os.getenv('ES_INDEX',default='meta_data')

    update_es = UpdateElastic(es_index)
    logger.info(f'Connected to elasticsearch with index: {es_index}')

    stt = SpeechToText()
    logger.info(f'Created an instance of Speech To Text')

    for doc in scan(update_es.es, index=update_es.index, query={"query": {"match_all": {}}},request_timeout=10000,scroll='25m'):
        id = doc['_id']
        file_path = update_es.get_file_path(id)
        text = stt.convert_from_path(file_path)
        logger.info(f'Created a text from audio for file: {doc['_source']['File_Name']}')

        update_es.update_doc(document={'audio_text': text},id=id)
        logger.info(f'Added the text for id:{id} to the document')

except Exception as e:
    logger.error(f'Did not work, error is: {e}')