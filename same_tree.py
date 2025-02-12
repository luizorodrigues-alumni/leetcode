# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def isSameTree(p , q) -> bool:
    if p == None and q == None:
        print("True!!")
        return True
    if p.val != q.val:
        print("False!!")
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


p = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
q = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
print(isSameTree(p, q))
