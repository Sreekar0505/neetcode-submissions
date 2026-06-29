class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        keyData = self.dic.get(key,{})
        keyData[timestamp] = value
        self.dic[key] = keyData

    def get(self, key: str, timestamp: int) -> str:
        keyData = self.dic.get(key,{})
        r = timestamp
        while r>0:
            if r in keyData:
                return keyData[r]
            r-=1
        return ''
