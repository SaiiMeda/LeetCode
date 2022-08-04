class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        out = 0
        x = 0
        
        for i in sorted(heights):
            if i != heights[x]:
                print(i,heights[x])
                out +=1
            x += 1
        return out
                
        
            
        