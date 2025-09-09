

class Criminal:
    def __init__(self,threshold):
        self.threshold = threshold

    def criminal(self,percentage):
        return percentage > self.threshold