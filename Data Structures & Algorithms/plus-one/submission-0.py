class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #first convert the list to a string
        string = "".join(str(digit) for digit in digits)

        #convert string to int and add one
        num = int(string) + 1

        #now split the num to list
        ans = [int(n) for n in str(num)]
        return ans

        