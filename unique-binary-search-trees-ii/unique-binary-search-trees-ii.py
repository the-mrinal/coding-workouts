# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees(start,end):
            if start > end:
                return [None,]
            
            all_trees = []
            
            for i in range(start,end + 1):
                left = generate_trees(start,i-1)
                
                right = generate_trees(i + 1,end)
                for l in left:
                    for r in right:
                        curr_tree = TreeNode(i)
                        curr_tree.left = l
                        curr_tree.right = r
                        all_trees.append(curr_tree)
                    
            return all_trees
            
        return generate_trees(1,n) if n else []
        