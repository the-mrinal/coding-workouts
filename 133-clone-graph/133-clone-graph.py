"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def __init__(self):
        self.visited = {}
    
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node is None:
            return 
        
        
        if node in self.visited:
            return self.visited[node]
        
        clone = Node(node.val,[])
        
        self.visited[node] = clone
        
        for n in node.neighbors:
            clone.neighbors.append(self.cloneGraph(n))
            
        
        return clone