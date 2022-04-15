#https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
#sets can't contain duplicates so if they're not equal then it means duplicates exist so it returns True.
