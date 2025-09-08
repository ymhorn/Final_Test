import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert_from_path(self,audio_file_path):
        with sr.AudioFile(audio_file_path) as audio:
            data = self.recognizer.record(audio)
            text = self.recognizer.recognize_google(data).lower()
        return text





