#Count Good Nodes in Binary Tree : https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count=0

        def helper(root, greatest):
            if root==None:
                return
            if root.val>=greatest:
                self.count+=1
                greatest=root.val
            helper(root.left,greatest)
            helper(root.right,greatest)

        helper(root,root.val)
        return self.count
