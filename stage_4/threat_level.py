

class ThreatLevel:
    def __init__(self,low_threshold,high_threshold):
        self.low_threshold = low_threshold
        self.high_threshold = high_threshold

    def threat_level(self,percentage):
        if percentage > self.high_threshold:
            return 'High'
        elif percentage > self.low_threshold:
            return 'Medium'
        else:
            return 'Low'