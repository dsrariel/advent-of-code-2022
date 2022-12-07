FILEPATH = "06.input"


class Counter(dict):
    def __init__(self):
        self.total = 0

    def add(self, key):
        self.total += 1
        self[key] = self.get(key, 0) + 1

    def sub(self, key):
        self.total -= 1
        self[key] -= 1
        if self[key] == 0:
            del self[key]


def findStartMarker(string: str, marker_size: int) -> int:
    counter = Counter()
    for i, c in enumerate(string):
        counter.add(c)
        if counter.total > marker_size:
            counter.sub(line[i - marker_size])
        if len(counter) == marker_size:
            return i + 1
    return -1


# marker_size = 4
marker_size = 14
with open(FILEPATH) as f:
    for line in f.readlines():
        line = line.rstrip()
        print(findStartMarker(line, marker_size))
