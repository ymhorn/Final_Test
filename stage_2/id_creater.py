import hashlib

class IdCreate:
    @staticmethod
    def create_unique_id(file_path):
        with open(file_path,'rb') as file:
            hash_number = hashlib.file_digest(file,"sha256").hexdigest()
        return hash_number


