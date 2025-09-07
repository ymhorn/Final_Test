from pathlib import Path
import os
from time_converter import TimeConvert

class PathObject:
    def __init__(self,path):
        self.path = Path(path)

    def file_name(self):
        return self.path.name

    def file_path(self):
        return self.path

    def file_size(self):
        return os.stat(self.path).st_size

    def time_created(self):
        return TimeConvert.time_converter(os.path.getctime(self.path))

    def time_last_modified(self):
        return TimeConvert.time_converter(os.path.getmtime(self.path))

