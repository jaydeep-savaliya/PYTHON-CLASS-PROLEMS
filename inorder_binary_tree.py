class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorderTraversal(root):
    ans = []
    def inorder(node):
        if node:
            inorder(node.left)
            ans.append(node.data)
            inorder(node.right)
    inorder(root)
    return ans

if __name__ == '__main__':
    root = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)
    ans=inorderTraversal(root)
    print(ans)
