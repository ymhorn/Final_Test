from datetime import datetime

class TimeConvert:
    @staticmethod
    def time_converter(original_time_format):
        time = datetime.fromtimestamp(original_time_format)
        return time