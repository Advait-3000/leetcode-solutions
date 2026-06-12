# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def paths(root, path):
            if not root:return
            if path!="":path=path+"->"+str(root.val)
            else:path=str(root.val)
            if not root.left and not root.right:
                ans.append(path)
                return
            paths(root.left, path)
            paths(root.right, path)
        paths(root, "")
        return ans