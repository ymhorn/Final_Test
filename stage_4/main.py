from base64_decode import Decoder
from percentage_calculater import PercentageCalculate
from criminal import Criminal
from count_words import CountWords
from elastic import UpdateElastic
from threat_level import ThreatLevel
import os
from stage_log.logging_file import Logger
from elasticsearch.helpers import scan

logger = Logger.get_logger()

try:
    hostile_list = os.getenv('HOSTILE_LIST',default='R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT')
    semi_hostile_list = os.getenv('SEMI_HOSTILE_LIST',default='RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==')
    divide_text_by = os.getenv('DIVIDE_TEXT_BY',default=33)
    threat_threshold = os.getenv('CRIMINAL_THRESHOLD',default=50)
    low_threshold = os.getenv('LOW_THRESHOLD',default=33)
    high_threshold = os.getenv('HIGH_THRESHOLD',default=66)
    es_index = os.getenv('ES_INDEX',default='meta_data')

    hostile = Decoder.decode_to_list(hostile_list)
    logger.info('Decoded hostile list')

    semi_hostile = Decoder.decode_to_list(semi_hostile_list)
    logger.info('Decoded semi-hostile list')

    percent = PercentageCalculate(divide_text_by)
    criminal_threshold = Criminal(threat_threshold)
    threat_threshold = ThreatLevel(low_threshold,high_threshold)

    update_es = UpdateElastic(es_index)
    logger.info(f'Connected to elasticsearch with index: {es_index}')

    for doc in scan(update_es.es, index=update_es.index, query={"query": {"match_all": {}}},request_timeout=10000,scroll='25m'):
        id = doc['_id']
        text = doc['_source']['audio_text']
        amount_semi_hostile = CountWords.count_words_in_text(semi_hostile,text)
        amount_hostile = CountWords.count_words_in_text(hostile,text) * 2
        sum_hostility = amount_semi_hostile + amount_hostile
        percent_score = percent.calculate(text,sum_hostility)

        document = {'bds_percent' : percent_score,
                    'is_bds' : criminal_threshold.criminal(percent_score),
                    'threat_level' : threat_threshold.threat_level(percent_score)}
        logger.info(f'Info ready to be added for document with id: {id}')

        update_es.update_doc(document=document,id=id)
        logger.info(f'Added the info for id:{id} to the document')

except Exception as e:
    logger.error(f'Did not work, error is: {e}')





