class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsComp = set(nums)
        if len(numsComp) != len(nums):
            return True
        return False