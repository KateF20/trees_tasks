class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        def traverse(root):
            if not root: # if a root is empty
                return 0

            else:
                height_l = traverse(root.left) # otherwise recursively get max depth/height of the left branch
                height_r = traverse(root.right) # and of the right
                # count max diameter at every step + compare it to current max diameter
                self.diameter = max(self.diameter, height_r + height_l)
                return max(height_l, height_r) + 1

        self.diameter = 0 # set current max diameter to 0
        traverse(root) # traverse through the whole tree
        return self.diameter


solution = Solution()
# input root = [1,2,3,4,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(solution.diameterOfBinaryTree(root)) # output 3