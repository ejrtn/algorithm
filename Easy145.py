# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        a = []
        a = Solution.con(self, root,a)
        print(a)
        return a
    def con(self, root, a):
        if root is not None:
            if root.left is not None:
                a = self.con(root.left,a)
                if root.right is not None:
                    a = self.con(root.right,a)
                
            else:
                if root.right is not None:
                    a = self.con(root.right,a)
                else:
                    a.append(root.val)
                    return a
        else:
            return a
        
        a.append(root.val)
        return a