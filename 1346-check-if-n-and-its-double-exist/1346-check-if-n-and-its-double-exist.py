class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dict_1 = {}
        for i in arr:
            if i in dict_1:
                return True
            elif i*2 in dict_1.values():
                return True
            if i not in dict_1:
                dict_1[i*2] = i
        return False
            
            
        