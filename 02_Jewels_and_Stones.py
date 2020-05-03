# may leetcode challange - Day 2
# problem - Jewels and Stones

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in S:
            if i in J :
                count += 1
        return count
