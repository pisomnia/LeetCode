import random
class RandomizedSet(object):
## List+Hashmap
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums=[]
        self.pos={}
        
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val]=len(self.nums)-1
            return True
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False
        idx,last=self.pos[val],self.nums[-1]
        self.nums[idx],self.pos[last]=last,idx
        self.nums.pop()
        del self.pos[val]
        return True
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0,len(self.nums)-1)]