#https://leetcode.com/problems/product-of-array-except-self/submissions/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = 0
        zeros = 0
        for i in nums:
            if i != 0:
                if output == 0:
                    output += 1
                output *= i
            else:
                zeros += 1
        for i in range(len(nums)): 
            if zeros == 1:
                if nums[i] == 0:
                    nums[i] = output
                else:
                    nums[i] = 0
            elif zeros > 1:
                nums[i] = 0
            else:
                nums[i] = output//nums[i]
        return nums