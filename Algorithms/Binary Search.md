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


## Template I
Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it)
No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found

- Initial Condition: left = 0, right = length-1
- Termination: left > right
- Searching Left: right = mid-1
- Searching Right: left = mid+1

## Template II
It is used to search for an element or condition which requires accessing the current index and its immediate right neighbor's index in the array.


## Template III



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