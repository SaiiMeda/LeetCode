class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        queue_1 = []
        for i in range(0,len(arr)):
            if arr[i] == 0:
                queue_1.append(0)
                queue_1.append(0)
                arr[i] = queue_1.pop(0)
            else:
                queue_1.append(arr[i])
                arr[i] = queue_1.pop(0)
        