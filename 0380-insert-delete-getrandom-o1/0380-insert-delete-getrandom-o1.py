class RandomizedSet:
    def __init__(self):
        self.random=[]
        self.freq={}
    def insert(self, val: int) -> bool:
        if val not in self.freq or self.freq[val]==0:
            self.random.append(val)
            self.freq[val]=1
            return True
        return False
    def remove(self, val: int) -> bool:
        if val in self.random:
            self.random.remove(val)
            self.freq[val]-=1
            return True
        return False
    def getRandom(self) -> int:
        return self.random[random.randint(0,len(self.random)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()