from pathlib import Path
import os
from stage_1.time_converter import TimeConvert

class PathObject:
    def __init__(self,path):
        self.path = Path(path)

    def file_name(self):
        return self.path.name

    def file_path(self):
        return str(self.path)

    def file_size(self):
        return os.stat(self.path).st_size

    def time_created(self):
        return str(TimeConvert.time_converter(os.path.getctime(self.path)))

    def time_last_modified(self):
        return str(TimeConvert.time_converter(os.path.getmtime(self.path)))

