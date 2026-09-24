class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        prefix,suffix = 0,0
        n = len(nums)
        for i in range(n):
            prefix = (prefix or 1)*nums[i]
            suffix = (suffix or 1)*nums[n-1-i]
            ans = max(ans,prefix,suffix)
        return ans

        