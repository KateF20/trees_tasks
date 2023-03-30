class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        if root is None: # if root is empty
            return True
        else:
            # get max depth of both branches
            depth_l = self.maxDepth(root.left)
            depth_r = self.maxDepth(root.right)

            # checking whether neither of branches is different from it's counterpart for more than 1
            if abs(depth_l - depth_r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False

    # func to get max depth of a root
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            depth_l = self.maxDepth(root.left)
            depth_r = self.maxDepth(root.right)
            return max(depth_l, depth_r) + 1


solution = Solution()
# input root = [3,9,20,null,null,15,7] --> output True
# input root = [1,2,2,3,3,null,null,4,4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
# output False
print(solution.isBalanced(root))