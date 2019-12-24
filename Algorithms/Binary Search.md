# Related Problems
```diff
- leetcode 1. Two Sum  
- lintcode 610. Two Sum - Difference equals to target  
- leetocde 560. Subarray Sum Equals K  
- leetcode 209. Minimum Size Subarray Sum  
- leetcode 325. Maximum Size Subarray Sum Equals k
- lintcode 533. Two Sum - Closest to target
- leetcode 15. 3Sum
```
## Two Sum - Difference equals to target

### Method 1
HashMap
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        for i in range(len(nums)):
            sum=target+nums[i]
            if sum in dict:
                return [dict[sum],i]
            diff=nums[i]-target
            if diff in dict:
                return [dict[diff],i]
            dict[nums[i]]=i
        return []
```

                    right-=1