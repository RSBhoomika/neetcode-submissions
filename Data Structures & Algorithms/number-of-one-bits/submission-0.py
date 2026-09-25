from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_rep = '{:32b}'.format(n)
        count = Counter(binary_rep)
        for num,freq in count.items():
            if num == '1':
                return int(freq)
        