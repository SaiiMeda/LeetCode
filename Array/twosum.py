class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} #keep track of the difference between target and current int
        for i,n in enumerate(nums):
            # i is the index, n is the value in the index
            difference = target - n
            if difference in dict: # if difference in dict just return indexes
                return(dict[difference], i) # since one unique solution always exists
            dict[n] = i
