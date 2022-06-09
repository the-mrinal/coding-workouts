# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        height = None
        def dfs(root):
            nonlocal height
            st = [[root,0]]
            count = 0
            while st:
                curr,l = st.pop()
                
                
                if curr.right:
                    st.append([curr.right,l+1])
                    
                else:
                    if height and height == l - 1:
                        return count
                
                if curr.left:
                    st.append([curr.left,l+1])
                else:
                    # we reached leaf node.
                    if height == l - 1:
                        return count
                
                if not curr.right and not curr.left:
                    if not height:
                        height = l
                    if height == l:
                        count += 1

            
            
            return count
        
        count = dfs(root)
        print(count,height)
        numberNode = (2 ** (height)) - 1 + count
        return numberNode
            
            