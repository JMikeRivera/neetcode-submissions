class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # empty list edge case
        if len(nums) == 0:
            return 0
        
        found = {}
        start = []
        longest = []
        res = 0
        
        # populate hasmap
        for i in range(len(nums)):
            if nums[i] in found:
                found[nums[i]] += 1
            else:
                found[nums[i]] = 1
        
        print(found)

        for i in range(len(nums)):
            if (nums[i]) - 1 not in found:
                start.append(nums[i])

        print(start)

        i = 0
        while i < len(start):
            if start[i] + 1 in found:
                start[i] += 1
                longest.append(start[i])
                if len(longest) > res:
                    res += 1
            else:
                i += 1
                longest.clear()

        #print(longest)
        #print(res)
        return res + 1
                
        