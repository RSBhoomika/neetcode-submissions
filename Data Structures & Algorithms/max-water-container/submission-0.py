class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currarea  = 0
        maxarea = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            currarea = min(heights[left],heights[right])*(right - left)
            maxarea = max(maxarea,currarea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return maxarea
        