#153 : https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxn, = nums[0],nums[0]
        
        result = maxn
        for i in range(1,len(nums)):
            cur = nums[i]
            tempmax = max(cur,maxn * cur,minn * cur)
            minn = min(cur,maxn * cur,minn * cur)
            maxn = tempmax
            result = max(maxn,result)
        return result
            