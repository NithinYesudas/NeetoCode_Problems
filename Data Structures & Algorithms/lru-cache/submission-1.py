class LRUCache:

    def __init__(self, capacity: int):
        self.mem = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        val = self.mem.get(key,-1)
        if val != -1:
            del self.mem[key]
            self.mem[key] = val 
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.mem:
            del self.mem[key]
        elif len(self.mem) == self.capacity:
            for curKey in self.mem:
                del self.mem[curKey]
                break
        self.mem[key] = value