# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans, levels = [], [root]
        
        while levels:
            ans.append([node.val for node in levels])
            temp = []
            for node in levels:
                temp.extend([node.left,node.right])
            levels = [leaf for leaf in temp if leaf]
        return ans