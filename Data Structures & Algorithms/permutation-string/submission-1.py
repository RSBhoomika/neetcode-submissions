#Main easy Answer
# import itertools
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         permutations = ["".join(p) for p in itertools.permutations(s1)]

#         found = False
#         for perm in permutations:
#             if perm in s2:
#                 found = True
#         return found

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: if s1 is longer than s2, a permutation cannot exist inside s2
        if len(s1) > len(s2):
            return False
            
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:len(s1)])
        
        # Check the very first window
        if s1_counts == window_counts:
            return True
            
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Add the character entering from the right
            char_enter = s2[i]
            window_counts[char_enter] += 1
            
            # Remove the character leaving from the left
            char_leave = s2[i - len(s1)]
            window_counts[char_leave] -= 1
            
            # Python's dict comparison fails if extra keys have a 0 count.
            # Clean up the key to keep comparison correct.
            if window_counts[char_leave] == 0:
                del window_counts[char_leave]
                
            # Compare the maps
            if window_counts == s1_counts:
                return True
                
        return False

        
        