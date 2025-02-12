from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root):
    """
    Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
    
    This approach uses a breadth-first search to traverse the tree and calculate the average of each level.
    The BFS(Breadth-First Search) returns an array of arrays, for instance, [[3], [9, 20], [15, 7]].
    """

    tree_queue = deque()
    tree_queue.append(root)
    bfs_result = []

    # Implementation of Tree Level Order Traversal using BFS ->
    while tree_queue:
        level = []
        n = len(tree_queue)

        for i in range(n):
            node = tree_queue.popleft()
            if node.left:
                tree_queue.append(node.left)
            if node.right:
                tree_queue.append(node.right)
            
            level.append(node.val)
        
        bfs_result.append(level)
    
    # Calculate the average of each level
    result = []
    for level in bfs_result:
        n = len(level)
        avg = 0
        for value in level:
            avg += value
        result.append(avg/n)
    
    return result
            