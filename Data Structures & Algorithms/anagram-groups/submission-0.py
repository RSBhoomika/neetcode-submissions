from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagram[sorted_s].append(s)
        return list(anagram.values())

        