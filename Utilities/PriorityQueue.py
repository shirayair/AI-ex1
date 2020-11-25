import heapq


class PriorityQueue:

    def __init__(self, f=lambda x: x):
        self.heap = []  # data structure to find min priority
        self.f = f
        self.hash_map = {}  # data structure to get to nodes in O(1)

    def append(self, item):
        heapq.heappush(self.heap, (self.f(item), item))
        self.hash_map[item.state] = item

    def extend(self, items):
        for item in items:
            self.append(item)

    def pop(self):
        if self.heap:
            node = heapq.heappop(self.heap)[1]
            del self.hash_map[node.state]
            return node
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def __len__(self):
        return len(self.heap)

    def __contains__(self, key):
        return key.state in self.hash_map

    def __getitem__(self, key):
        for value, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the priority queue")

    def __delitem__(self, key):
        try:
            del self.heap[[item == key for _, item in self.heap].index(True)]
            del self.hash_map[key.state]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)

    def __repr__(self):
        return str(self.heap)
