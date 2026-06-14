# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def frequency(self, root, freq):
        if not root:return
        if root.val not in freq:freq[root.val]=1
        else:freq[root.val]+=1
        self.frequency(root.left, freq)
        self.frequency(root.right, freq)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq={}
        self.frequency(root, freq)
        maxFreq=0
        res=[]
        for i in freq:
            if freq[i]>maxFreq:
                res=[i]
                maxFreq=freq[i]
            elif freq[i]==maxFreq:res.append(i)
        return res