class MyHashMap:

    def __init__(self):
        self.capacity = 10000
        self.hashMap = [-1]*self.capacity
        

    def put(self, key: int, value: int) -> None:
        pos = key%self.capacity
        self.hashMap[pos] = value

        

    def get(self, key: int) -> int:
        pos = key%self.capacity
        return self.hashMap[pos]
        

    def remove(self, key: int) -> None:
        pos = key%self.capacity
        self.hashMap[pos]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)