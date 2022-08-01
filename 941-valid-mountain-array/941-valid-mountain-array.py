class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        up = True
        if len(arr) == 2:
            return False
        for i in range(1,len(arr)):
                
            if arr[i-1] == arr[i]:
                return False
            if up:
                if arr[i - 1] > arr[i]:
                    up = False
            else:
                if i == 2:
                    return False
                if arr[i - 1] < arr[i]:
                    return False
        if up:
            return False
        return True
                
            
        