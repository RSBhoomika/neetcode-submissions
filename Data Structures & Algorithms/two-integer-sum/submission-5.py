class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()

        left = 0
        right = len(arr) - 1

        while left < right:
            currsum = arr[left][0] + arr[right][0]

            if currsum == target:
                return [arr[left][1], arr[right][1]]
            elif currsum < target:
                left += 1
            else:
                right -= 1

        return []