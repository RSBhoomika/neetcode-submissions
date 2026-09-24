import itertools
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutations = ["".join(p) for p in itertools.permutations(s1)]

        found = False
        for perm in permutations:
            if perm in s2:
                found = True
        return found
        
        