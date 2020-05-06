# May leetcode Challange day- 6
# problem- Majority Element


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)           #count the number of each element in the array
        for i in range(n):              #itereate over the dict to find Majority Element
            c = count[nums[i]]
            if c > n//2:
                return nums[i]          #return the element from array when found
