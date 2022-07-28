# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        rootString = ""
        destString = ""
        stack = [[root,""]]
        
        while stack:
            curr,currString = stack.pop()
            
            if curr.val == startValue:
                rootString = currString
            elif curr.val == destValue:
                destString = currString
            
            if curr.left:
                stack.append([curr.left,currString+"L"])
            if curr.right:
                stack.append([curr.right,currString+"R"])
        
        
        index1 = 0
        index2 = 0
        while index1 < len(rootString) and index2 < len(destString) and rootString[index1] == destString[index2]:
            index1 += 1
            index2 += 1
        
        rootString = rootString[index1:]
        destString = destString[index2:]
        res = "U"*len(rootString)+destString
        return res