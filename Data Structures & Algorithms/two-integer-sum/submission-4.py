class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            currsum = nums[left] + nums[right]
            if currsum == target:
                break
            elif currsum < target:
                left += 1
            else:
                right -=1
        return [left,right]