# Related Problems
```diff
- leetcode 33. Search in Rotated Sorted Array
- lintcode 153. Find Minimum in Rotated Sorted Array
- leetocde 
- leetcode 
- leetcode 
- lintcode 
- leetcode 
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
Gurantees Search Space is at least 2 in size at each step.
Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition

- Initial Condition: left = 0, right = length
- Termination: left == right
- Searching Left: right = mid
- Searching Right: left = mid+1
- Post-processing: need


## Template III
It is another unique form of Binary Search. It is used to search for an element or condition which requires accessing the current index 
and its immediate left and right neighbor's index in the array.
Gurantees Search Space is at least 3 in size at each step
Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.

- Initial Condition: left = 0, right = length-1
- Termination: left + 1 == right
- Searching Left: right = mid
- Searching Right: left = mid
- Post-processing: need

## Search in Rotated Sorted Array

### Method 
Template I
```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<0:
            return -1
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)/2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:
                if target>=nums[left] and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if target<nums[left] and target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
```




## Find Minimum in Rotated Sorted Array

### Method 
Template II
```python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left]<nums[right]:
                return nums[left]
            mid=left+(right-left)//2
            
            if nums[mid]>=nums[left]:
                left=mid+1
            else:
                right=mid
        return nums[left]
```
