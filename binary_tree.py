class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
class Solution:
    def __init__(self,root):
        self.root = root
    # inorderTraversal
    def inorderTraversal(self,root:[TreeNode])->list[int]:
        ans = []
        def inorder(root):
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
        inorder(root)
        return ans
    # postordeTraversal
    def postorderTraversal(self, root: [TreeNode]) -> list[int]:
        ans = []
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                ans.append(root.val)
        postorder(root)
        return ans
    # preorderTRaversal
    def preorderTraversal(self, root:[TreeNode]) -> list[int]:
        ans = []
        def preorder(root):
            if root:
                ans.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ans
if __name__=='__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    solution = Solution(root)
    print(solution.inorderTraversal(root))
    print(solution.preorderTraversal(root))
    print(solution.postorderTraversal(root))