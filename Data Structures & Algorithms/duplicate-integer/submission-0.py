class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noRepeats = set(nums)
        if len(noRepeats) != len(nums):
            return True
        else: 
            return False
        