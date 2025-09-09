from base64_decode import Decoder
from percentage_calculater import PercentageCalculate
from criminal import Criminal
from count_words import CountWords
from elastic import UpdateElastic
from threat_level import ThreatLevel
import os
from stage_log.logging_file import Logger
from elasticsearch.helpers import scan

hostile = Decoder.decode_to_list('R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT')
semi_hostile = Decoder.decode_to_list('RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==')

percent = PercentageCalculate(33)
criminal_threshold = Criminal(50)
threat_threshold = ThreatLevel(33,66)

update_es = UpdateElastic('meta_data')

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
    update_es.update_doc(document=document,id=id)





