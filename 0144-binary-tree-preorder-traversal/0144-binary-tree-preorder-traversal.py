# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        current = root
        elements = []
        while root:
            if current:
                elements.append(current.val)
                stack.append(current)
                current = current.left
            elif stack:
                temp = stack.pop()
                current = temp.right
            else:
                break
        return elements
            