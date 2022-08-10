class Solution:
    def longestCommonPrefix(self, m: List[str]) -> str:
        if not m: return ''
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] 
        return s1
                
                
            
            