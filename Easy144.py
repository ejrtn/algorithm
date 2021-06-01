# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        
        
        a = []
        return Solution.con(self, root,a)
    def con(self, root, a):
        if root is not None:
            a.append(root.val)
            if root.left is not None:
                if root.right is not None:
                    return self.con(root.right,self.con(root.left,a))
                else:
                    return self.con(root.left,a)
            else:
                if root.right is not None:
                    return self.con(root.right,a)
                else:
                    return a
        else:
            return a
        


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        
        r = [root]
        rs = []
        a = []
        c = 0
        while(True):
            if r[c] is not None:
                a.append(r[c].val)
                for i in range(len(r)):
                    if i==c:
                        rs.append(r[i].left)
                        rs.append(r[i].right)
                    else:
                        rs.append(r[i])
                r=rs
                rs=[]
            else:
                c += 1
            if c>=len(r):
                return a