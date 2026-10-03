class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_count,close_count,curr_str):
            if open_count == n and close_count == n:
                res.append(curr_str)
                return

            if open_count < n:
                backtrack(open_count+1,close_count,curr_str+'(')
            
            if close_count < open_count:
                backtrack(open_count,close_count+1,curr_str+')')

        backtrack(0,0,"")
        return res
        