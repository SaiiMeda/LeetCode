class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        queue_1 = []
        for i in range(len(arr)):
            if queue_1 and arr[i] != 0:
                queue_1.append(arr[i])
                arr[i] = queue_1.pop(0)
            elif arr[i] == 0:
                queue_1.append(0)
                queue_1.append(0) 
                arr[i] = queue_1.pop(0)
                
                
                
                    
                
                