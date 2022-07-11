class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i,n in enumerate(numbers):
            # i is the index, n is the value in the index
            difference = target - n
            if difference in dict:
                return(dict[difference] + 1, i +1)
            dict[n] = i
        print(dict)
            