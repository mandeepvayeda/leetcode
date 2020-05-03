# May leetcode challange day-1
#problem - First Bad Version


class Solution:
    def firstBadVersion(self, n):
        if n<2:
            return n
        start = 1
        end = n
        while start <= end:
            mid  = (start + end)//2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid - 1):
                end = mid - 1
            else:
                start  = mid + 1
