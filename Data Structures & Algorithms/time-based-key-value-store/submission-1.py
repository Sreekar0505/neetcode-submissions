from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.dic = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        timestamps = self.dic[key]
        idx = timestamps.bisect_right(timestamp) - 1

        if idx >= 0:
            closest_time = timestamps.iloc[idx]
            return timestamps[closest_time]
        return ''
