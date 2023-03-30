'''
LeetCode 226. Invert Binary Tree (easy)
Given the root of a binary tree, invert the tree, and return its root.
'''


# provided by LeetCode
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
class Solution(object):
    def invertTree(self, root):
        if root is None: # for a leaf node with no children
            return None

        root.right, root.left = root.left, root.right # if there are, we swap them
        self.invertTree(root.left) # recursively do this for all the left subtrees
        self.invertTree(root.right) # and the right

        return root


solution = Solution()
# Input: root = [4,2,7,1,3,6,9]

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Output: [4,7,2,9,6,3,1]
inverted_root = solution.invertTree(root)
