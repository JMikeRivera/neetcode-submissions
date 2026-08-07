class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # water = min(height 1, height2) * distance(height1, height2)
        # distance is measured by index
        i, j = 0, len(heights) - 1
        currentArea = 0

        while i < j:
            width = j - i
            height = min(heights[i], heights[j])
            area = width * height
            if heights[i] > heights[j]:
                j -= 1
            else: i += 1
            if area > currentArea:
                currentArea = area
        
        return currentArea