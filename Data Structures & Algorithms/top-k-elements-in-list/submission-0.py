class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # implementation of bucket sort
        buckets = [[] for _ in range(len(nums) + 1)]
        frequencies = {}
        result = []
        
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        for number, frequency in frequencies.items():
            buckets[frequency].append(number)

        for frequency in range(len(buckets) -1, 0, -1):
            for number in buckets[frequency]:
                result.append(number)

                if len(result) == k:
                    return result

        