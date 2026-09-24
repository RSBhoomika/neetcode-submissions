class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}':'{',']':'[',')':'('}
        stack = []

        for ch in s:
            if ch in mapping:
                if stack:
                    top_elem = stack.pop()

                    if mapping[ch] != top_elem:
                        return False
            else:
                stack.append(ch)
        return not stack

        