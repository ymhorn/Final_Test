

class CountWords:
    @staticmethod
    def count_words_in_text(list_of_words,text):
        word_count = 0
        for word in list_of_words:
            if word.lower() in text:
                word_count += 1
        return word_count


