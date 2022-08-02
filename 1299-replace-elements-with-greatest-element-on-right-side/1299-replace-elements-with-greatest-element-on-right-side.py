class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current = 0
        for i in range(len(arr)-1,-1,-1):
            if i == (len(arr) - 1):
                current = arr[i]
                arr[i] = -1
                
            else:
                if arr[i] > current:
                    print(current)
                    arr[i],current = current,arr[i]
                    print("after",current)
                else:
                    arr[i] = current
        return arr

        