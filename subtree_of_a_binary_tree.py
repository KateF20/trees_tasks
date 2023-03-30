class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root: # check if there is a tree and a subtree
            print('x')
            return False
        if root.val == subRoot.val and self.is_same(root, subRoot): # check the head of both trees and their branches
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same(self, root_1, root_2):
        if not root_1 and not root_2:
            return True
        if not root_1 or not root_2:
            return False
        if root_1.val != root_2.val:
            return False
        return self.is_same(root_1.left, root_2.left) and self.is_same(root_1.right, root_2.right)


solution = Solution()
# input root = [3,4,5,1,2], subRoot = [4,1,2]
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(solution.isSubtree(root, subRoot))