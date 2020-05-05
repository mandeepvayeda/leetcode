# May leetcode challange day- 5
# problem- First Unique Character in a String


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s) #create a dict with count of chars in it
        for i in range(len(s)): #iterate over the dict to search first unique char
            if count[s[i]] == 1:
                return i #return its index if found
        return -1 
