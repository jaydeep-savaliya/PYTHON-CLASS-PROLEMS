import collections
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def levelordertraversal(root):
    if not root:
            return []
    result = []
    queue =collections.deque([root])
    while queue:
            level_values = []
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_values)
        
    return result
    
if __name__=='__main__':
     root = Node(3)
     root.left = Node(9)
     root.right = Node(20)
     root.right.left = Node(15)
     root.right.right = Node(7)
     ans = levelordertraversal(root)
     print(ans)