class Node:
    def __init__(self, data, key = None) -> None:
        self.key = key
        self.data = data
        self.right : Node = None
        self.left : Node = None

    def __str__(self) -> str:
        return f"{self.data}"

    def __repr__(self) -> str:
        return f"{self.key}: {self.data}"
    
class Tree:
    def __init__(self) -> None:
        self.root: Node = None

    def insert(self, value, key = None):
        if not self.root:
            self.root = Node(value, key)
        else:
            self._insert(value, self.root, key)

    def _insert(self, value, node : Node = None, key = None):
        # key = key if key else value
        if key < node.key:
            if node.left:
                self._insert(value, node.left, key)
            else:
                node.left = Node(value, key)
        else:
            if node.right:
                self._insert(value, node.right, key)
            else:
                node.right = Node(value, key)

def binary_search(value, node:Node, key = -1):
    if not node: 
        return False
    if node.data == value:
        return True
    if key < node.key:
        return binary_search(value, node.left, key)
    return binary_search(value, node.right, key)
        

def preorder(node : Node):
    txt = ""
    if node:
        txt += str(node) + ','
        txt += preorder(node.left)
        txt += preorder(node.right)
    return txt

def inorder(node : Node):
    txt = ""
    if node:
        txt += inorder(node.left)
        txt += str(node) + ','
        txt += inorder(node.right)
    return txt

def postorder(node : Node):
    txt = ""
    if node:
        txt += postorder(node.left)
        txt += postorder(node.right)
        txt += str(node) + ','
    return txt

if __name__ == "__main__":
    t = Tree()
    for x in  [50, 30, 70, 20, 40, 60, 80]:
        t.insert(x)
    print(inorder(t.root))
    print(preorder(t.root))
    print(postorder(t.root))
    print(binary_search(40, t.root))
    print(binary_search(100, t.root))
            