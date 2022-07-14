# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(start,end):
            nonlocal preorderIndex
            if start > end:
                return None

            value = preorder[preorderIndex]

            index = index_map[value]
            root = TreeNode(value)
            preorderIndex += 1
            root.left = helper(start,index - 1)

            root.right = helper(index + 1,end)


            return root

        index_map = {value:index for index,value in enumerate(inorder)}

        preorderIndex = 0

        return helper(0,len(preorder) - 1)

        