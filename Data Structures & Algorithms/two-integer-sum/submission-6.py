# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         left = 0
#         right = len(nums) - 1
#         while left < right:
#             currsum = nums[left] + nums[right]
#             if currsum == target:
#                 break
#             elif currsum < target:
#                 left += 1
#             else:
#                 right -=1
#         return [left,right]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()

        left = 0
        right = len(arr) - 1

        while left < right:
            currsum = arr[left][0] + arr[right][0]

            if currsum == target:
                i = arr[left][1]
                j = arr[right][1]
                return [min(i, j), max(i, j)]

            elif currsum < target:
                left += 1
            else:
                right -= 1

        return []