# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def recursiveTree(root1, root2):
            if not root1 and not root2:
                return None
            if root1 and not root2:
                return root1
            if not root1 and root2:
                return root2
            
            merged_node = TreeNode(val=root1.val + root2.val)            
            
            merged_node.left = recursiveTree(root1.left, root2.left)
            merged_node.right = recursiveTree(root1.right, root2.right)

            return merged_node
        
        return recursiveTree(root1, root2)

        

        



   