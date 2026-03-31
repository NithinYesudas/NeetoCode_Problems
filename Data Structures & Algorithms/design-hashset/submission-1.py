class MyHashSet:

    def __init__(self):
        self.maxCapacity = 10000
        self.hashset = [-1]*self.maxCapacity
        

    def add(self, key: int) -> None:
        pos = key%self.maxCapacity
        self.hashset[pos]=key

        

    def remove(self, key: int) -> None:
        pos = key%self.maxCapacity
        self.hashset[pos]=-1


        

    def contains(self, key: int) -> bool:
        pos = key%self.maxCapacity
        if self.hashset[pos]!=-1:
            return True
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)