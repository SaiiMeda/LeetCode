class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero, mx, j = 0, 0, 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero += 1
            while zero > 1:
                if nums[j] == 0:
                    zero -= 1
                j += 1
            mx = max(mx, i - j + 1)
        return mx