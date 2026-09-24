class Solution:
    def square(self,n):
        ans = 0
        while n > 0:
            digit = n%10
            ans += digit*digit
            n = n // 10
        return ans
    def isHappy(self, n: int) -> bool:
        slow = self.square(n)
        fast = self.square(self.square(n))

        while slow != fast:
            slow = self.square(slow)
            fast = self.square(self.square(fast))

            if fast == 1:
                return True
        return slow == 1
        