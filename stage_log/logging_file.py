import logging
from elasticsearch import Elasticsearch
from datetime import datetime
import os

logger_name = os.getenv('LOGGER_NAME',default="meta_data_logging")
elastic_host = os.getenv('ES_HOST',default="http://localhost:9200")
logger_index = os.getenv('LOGGER_INDEX',default="logs")

class Logger:
    _logger = None
    @classmethod
    def get_logger(cls, name=logger_name, es_host=elastic_host,
index=logger_index, level=logging.DEBUG):
        if cls._logger:
            return cls._logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            es = Elasticsearch(es_host)
            class ESHandler(logging.Handler):
                def emit(self, record):
                    try:
                        es.index(index=index, document={
                            "timestamp": datetime.utcnow().isoformat(),
                            "level": record.levelname,
                            "logger": record.name,
                            "message": record.getMessage()
                        })
                    except Exception as e:
                        print(f"ES log failed: {e}")
            logger.addHandler(ESHandler())
            logger.addHandler(logging.StreamHandler())
        cls._logger = logger
        return logger
