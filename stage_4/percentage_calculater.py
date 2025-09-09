

class PercentageCalculate:
    def __init__(self,divide_text_by):
        self.text_divider = divide_text_by

    def calculate(self,text,word_number):
        try:
            text_length = len(text.split(' '))
            return 100 * ((text_length/self.text_divider)/word_number)
        except ZeroDivisionError:
            return 0
