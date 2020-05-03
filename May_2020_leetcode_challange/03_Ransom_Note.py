# May leetcode challange day - 3
# problem - Ransom Note



class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        answer = len(Counter(ransomNote) - Counter(magazine))
        if not answer:
            return True
        else:
            return False
