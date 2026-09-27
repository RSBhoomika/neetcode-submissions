class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            currsum = numbers[left] + numbers[right]

            if target == currsum:
                return [left+1,right+1]
            
            elif target > currsum:
                left += 1
            else:
                right -= 1
        return []
        