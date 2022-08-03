class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                if zeros != 0:
                    nums[i-zeros] = nums[i]
                    nums[i] = 0