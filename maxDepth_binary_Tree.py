class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        counter = 0 # set a counter to count steps

        if root is None: # if root is empty
            return counter

        else:
            depth_r = self.maxDepth(root.right) # recursively call the function to get the max depth of the right branch
            depth_l = self.maxDepth(root.left) # and of the left
            counter = max(depth_r, depth_l) + 1 # find the max of them and add 1 for a current coot to count
            return counter

solution = Solution()
# input root = [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# output 3
print(solution.maxDepth(root))
