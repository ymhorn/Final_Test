

class JsonBuilder:
    def __init__(self,path):
        self.path = path

    def json(self):
        dict_info = {
            'File_Name' : self.path.file_name(),
            'File_Path' : str(self.path.file_path()),
            'File_Size' : self.path.file_size(),
            'Time_Created' : str(self.path.time_created()),
            'Time_Modified' : str(self.path.time_last_modified())
        }
        return dict_info