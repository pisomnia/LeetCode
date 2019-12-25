class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        hashmap ={}
        for task in tasks:
            hashmap[task]=hashmap.get(task,0)+1
        max_count =max(hashmap.values())
        k=0
        for task in hashmap.keys():
            if hashmap[task]==max_count:
                k+=1
        return max(len(tasks),(max_count-1)*(n+1)+k)