class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}':'{',']':'[',')':'('}
        stack = []

        for ch in s:
            if ch in mapping:
                top_element = stack.pop() if stack else '#'

                if mapping[ch] != top_element:
                    return False
            else:
                stack.append(ch)
        return not stack

        