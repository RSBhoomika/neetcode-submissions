class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            # Case 1: Odd-length palindromes (e.g., "aba", center is 'b')
            res += self.countPali(s, i, i)
            
            # Case 2: Even-length palindromes (e.g., "abba", center is between 'b' and 'b')
            res += self.countPali(s, i, i + 1)
            
        return res

    def countPali(self, s: str, l: int, r: int) -> int:
        count = 0
        # Expand outwards as long as pointers are in bounds and characters match
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1  # Move left pointer outward
            r += 1  # Move right pointer outward
        return count

        
        