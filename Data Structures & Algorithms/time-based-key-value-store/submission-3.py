class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        saved = ""
        left = 0
        right = len(self.store[key])

        while left < right:
            middle = (left + right) // 2

            if self.store[key][middle][0] > timestamp:
                right = middle
                
            elif self.store[key][middle][0] <= timestamp:
                saved = self.store[key][middle][1]
                left = middle + 1
                
        
        return saved
        
