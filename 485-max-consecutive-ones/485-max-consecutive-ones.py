class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x1 = 0 
        x2 = 0
        for i in nums:
            if i == 1:
                x1 += 1
                x2 = max(x1,x2)
            else:
                x1 = 0
                
        return x2