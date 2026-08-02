class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        import math
        
        res = []
        for i in range(len(nums)):
            bye = nums[i]
            nums.pop(i)
            res.append(math.prod(nums))
            nums.insert(i, bye)
        print(res)
        return res
        """
        res = []
        pre, post, i = 1, 1, 0
        print(nums)
        while i < len(nums):
            res.insert(i, pre)
            pre *= nums[i]
            i += 1
        
        while i > 0:
            i -= 1
            res[i] = res[i] * post
            post *= nums[i]
        
        return res