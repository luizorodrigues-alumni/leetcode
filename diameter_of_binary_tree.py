# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Armazena o maior diâmetro encontrado

        def maxDepth(node):
            if not node:
                return 0
            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)
            
            # Atualiza o diâmetro máximo se a soma das profundidades for maior
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Retorna a profundidade máxima do nó atual
            return 1 + max(left_depth, right_depth)
        
        maxDepth(root)
        return self.diameter
