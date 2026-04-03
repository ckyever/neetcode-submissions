class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        time_values = self.timemap.get(key, None)

        if time_values:
            left, right = 0, len(time_values) - 1
            result = ""

            while left <= right: 
                mid = (left + right) // 2

                if time_values[mid][0] > timestamp:
                    right = mid - 1
                elif time_values[mid][0] < timestamp:
                    result = time_values[mid][1]
                    left = mid + 1
                else:
                    return time_values[mid][1]
 
            return result
             
        else:
            return ""
        
