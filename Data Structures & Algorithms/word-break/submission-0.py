from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)

        @cache
        def can_split(remaining_string:str) -> bool:
            if not remaining_string:
                return True
            
            for i in range(1,len(remaining_string)+1):
                prefix = remaining_string[:i]
                suffix = remaining_string[i:]

                if prefix in wordset and can_split(suffix):
                    return True
            
            return False
        return can_split(s)