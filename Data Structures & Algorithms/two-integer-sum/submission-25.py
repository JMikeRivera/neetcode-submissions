class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            search = target - nums[i]
            if search in dictionary:
                return sorted([i, dictionary[search]])
            else:
                dictionary[nums[i]] = i
            