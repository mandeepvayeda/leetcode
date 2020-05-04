# May leetcode challange day- 4
# problem - Number Complement


class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        int_binary = ''.join(['1'] * len(binary))
        return num ^ int(int_binary, 2)
