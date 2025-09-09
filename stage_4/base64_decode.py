import base64

class Decoder:
    @staticmethod
    def decode_to_list(code):
        return base64.b64decode(code).decode('UTF-8').split(',')
