class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None: # if both trees are empty
            return True

        if p is None or q is None: # if one of the trees is empty
            return False

        # if current subtrees and all their branches are equal
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False


solution = Solution()
# input roots p = [1,2,3], q = [1,2,3]
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
# output True
print(solution.isSameTree(p, q))