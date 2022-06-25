"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cached = {}
        def bfs(node):
            if node is None:
                return None

            if node in cached:
                return cached[node]
            
            new_node = Node(node.val,[])
            cached[node] = new_node

            for neigh in node.neighbors:
                new_node.neighbors.append(bfs(neigh))

            return new_node
        return bfs(node)
