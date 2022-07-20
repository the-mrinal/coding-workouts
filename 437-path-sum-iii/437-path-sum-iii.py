# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        hashMap = defaultdict(int)
        def preorderTraversal(node,currSum):
            nonlocal count,hashMap
            if not node:
                return 0
            currSum += node.val
            if currSum == targetSum:
                count += 1
                
            count += hashMap[currSum - targetSum]
            
            hashMap[currSum] += 1
            
            preorderTraversal(node.left,currSum)
            preorderTraversal(node.right,currSum)
            
            hashMap[currSum] -= 1
        
        preorderTraversal(root,0)
        return count
