class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        y = abs(x)
        y = str(y)
        y = y[::-1]

        ans = int(y)*sign

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans
        