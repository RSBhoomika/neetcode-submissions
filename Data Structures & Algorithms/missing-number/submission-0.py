class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        comp = [i for i in range(n+1)]

        ans = list(set(comp) - set(nums))
        return ans[0]
        