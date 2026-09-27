# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         n = len(nums)
#         ans = []

#         for i in range(n - 2):
#             for j in range(i + 1, n - 1):
#                 for k in range(j + 1, n):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         triplet = [nums[i], nums[j], nums[k]]

#                         if triplet not in ans:
#                             ans.append(triplet)

#         return ans

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate first values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # If the smallest possible sum is > 0,
            # everything after this is also > 0.
            if nums[i] > 0:
                break

            # If the largest possible sum is < 0,
            # move to the next i.
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                currsum = nums[i] + nums[left] + nums[right]

                if currsum == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif currsum < 0:
                    left += 1
                else:
                    right -= 1

        return ans