# Related Problems
leetcode 1. Two Sum \
lintcode 610. Two Sum - Difference equals to target \
leetocde 560. Subarray Sum Equals K \
leetcode 209. Minimum Size Subarray Sum \
leetcode 15. 3Sum

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
### Method 2
Double Pointers 
- 主动指针R 
- 被动指针L 
- for (R=0;R<n;R++) \
----while (A[R]-A[L]>target) \
------L++ 
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        new_nums=[(num,i) for i,num in enumerate(nums)]
		target=abs(target)
		n,indexs=len(nums),[]
		new_nums.sort(key=lambda x:x[0])
		i=0
        for j in range(len(nums)):
			if i==j:
				j+=1
			while i<j and (new_nums[j][0]-new_nums[i][0])>  target:
				i+=1
			if i<j and (new_nums[j][0]-new_nums[i][0]) == target:
				indexs=[new_nums[i][1], new_nums[j][1]]
				break
		if indexs[0]>indexs[1]:
			indexs[0],indexs[1] = indexs[1],indexs[0]
		return indexs
```

## Subarray Sum Equals K
### Method
Prefix sum and hashmap



## Minimum Size Subarray Sum

## 3Sum
