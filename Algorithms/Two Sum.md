# Related Problems
leetcode 1. Two Sum \
lintcode 610. Two Sum - Difference equals to target \
leetocde 560. Subarray Sum Equals K \
leetcode 209. Minimum Size Subarray Sum \
leetcode 15. 3Sum

## <font color=red> Two Sum - Difference equals to target </font>

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

for(R=0;R<n;R++)  
    while (A[R]-A[L]>target)  
        L++  

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

## <font color=red> Subarray Sum Equals K </font>
### Method
Prefix Sum and HashMap
```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums)==0:
            return 0
        sum_num =[0]*len(nums)
        sum_num[0]=nums[0]

        for i in range(1,len(nums)):
            sum_num[i]=sum_num[i-1]+nums[i]
        res=0
        dic={}
        dic[0]=1
        for i in range(len(sum_num)):
            if (sum_num[i]-k) in dic:
                res+=dic[sum_num[i]-k]
            dic[sum_num[i]]=dic.get(sum_num[i],0)+1
        return res
```


## <font color=red> Minimum Size Subarray Sum </font>
### Method
Double Pointers
```python
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        n = len(nums)
        minLength = n + 1
        sum = 0
        j = 0
        for i in range(n):
            while j < n and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                minLength = min(minLength, j - i)

            sum -= nums[i]
            
        if minLength == n + 1:
            return 0
            
        return minLength
```

## <font color=red> 3Sum </font>
