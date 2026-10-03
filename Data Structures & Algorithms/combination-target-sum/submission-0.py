class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(remain,combo,start_index):
            if remain == 0:
                res.append(list(combo))
                return 

            for i in range(start_index,len(nums)):
                if nums[i] > remain:
                    break 
                combo.append(nums[i])
                backtrack(remain-nums[i],combo,i)
                combo.pop()
        backtrack(target,[],0)
        return res
        