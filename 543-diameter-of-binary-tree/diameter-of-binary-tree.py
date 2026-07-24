# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 #initializing the diameter to 0

        def dfs(cur):
            if not cur:
                return 0
            # using the post-order dfs traversal
            left = dfs(cur.left)
            right = dfs(cur.right)

            self.res = max(self.res, left+right)  #update the current diameter

            return 1+max(left, right)   #return the height
        
        dfs(root)
        return self.res
        