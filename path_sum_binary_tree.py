# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum) -> bool:
    if root is None:
        return False
    
    if root.left is None and root.right is None:
        if root.val == targetSum:
            return True
        else:
            return False
    
   
    return hasPathSum(root.left, targetSum-root.val) or hasPathSum(root.right, targetSum-root.val)
    

root = TreeNode(val=5, left=TreeNode(val=4, left=TreeNode(val=11, left=TreeNode(val=7), right=TreeNode(val=2))), right=TreeNode(val=8, left=TreeNode(val=13), right=TreeNode(val=4, right=TreeNode(val=1))))
print(hasPathSum(None, 22))