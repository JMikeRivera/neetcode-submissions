class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        
        res = []
        for i in range(len(nums)):
            bye = nums[i]
            nums.pop(i)
            res.append(math.prod(nums))
            nums.insert(i, bye)
        print(res)
        return res