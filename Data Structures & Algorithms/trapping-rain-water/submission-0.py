class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        trappedWater = 0
        suffixMax, prefixMax = [0] * n, [0] * n
        # last element is always itself for suffix
        suffixMax[n - 1] = height[n - 1]
        # fist element is always itself for prefix
        prefixMax[0] = height[0]
        # filling the arrays
        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(height[i], suffixMax[i + 1])
        for i in range(n):
            prefixMax[i] = max(height[i], prefixMax[i - 1])

        for i in range(n):
            trappedWater += min(suffixMax[i], prefixMax[i]) - height[i]
        
        return trappedWater