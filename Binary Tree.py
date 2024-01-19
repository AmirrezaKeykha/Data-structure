class BinaryTree:
    def __init__(self,data):
        self.valed=data
        self.leftchild=None
        self.rightchild=None
        
    # Insert data to binary search tree    
    def insert_BST(self,data):
        if self.valed:
            if data < self.valed:
                if self.leftchild is None:
                    self.leftchild=BinaryTree(data)
                else:
                    self.leftchild.insert(data)
            elif data > self.valed:
                if self.rightchild is None:
                    self.rightchild=BinaryTree(data)
                else:
                    self.rightchild.insert(data)
        else:
            self.valed=BinaryTree(data)  # If no data already exists 
    
    # Insert data to binary tree
    def insert(self,data):
        if self.valed:
            if self.leftchild is None:
                self.leftchild=BinaryTree(data)
            else:
                self.leftchild.insert(data)
        else:
            self.valed=BinaryTree(data)

    # Preorder traversal of binary tree                 
    def preordrer(self):
        print(self.valed,end=" ")
        if self.leftchild:
            self.leftchild.preordrer()
        if self.rightchild:
            self.rightchild.preordrer()
    
    # Inorder traversal of binary tree
    def inorder(self):
        if self.leftchild:
            self.leftchild.inorder()
        print(self.valed,end=" ")
        if self.rightchild:
            self.rightchild.inorder()
    
    # Postorder traversal of binary tree        
    def postorder(self):
        if self.leftchild:
            self.leftchild.postorder()
        if self.rightchild:
            self.rightchild.postorder()
        print(self.valed,end=" ")

    # Delete data from binary tree
    def delete(self,data):
        if data > self.valed:
            self.rightchild.delete(data)
        elif data < self.valed:
            self.leftchild.delete(data)
        elif data == self.valed:
            self.valed=10     # For example change data to 10
            
# Return number of nodes of binary tree
def countofnodes(tree):
    if tree:
        return countofnodes(tree.leftchild)+countofnodes(tree.rightchild)+1
    else:
        return False

# Return number of  leaf nodes of binary tree        
def countofleafnodes(tree):
    if tree is None:
        return 0  # Tree empty 
    if (tree.leftchild is None and tree.rightchild is None):
        return 1  # Just root exist
    else:
        return countofleafnodes(tree.leftchild) + countofleafnodes(tree.rightchild)

# Return sum of nodes of binary tree    
def sumofnodes(tree):
    if tree:
        return sumofnodes(tree.leftchild)+sumofnodes(tree.rightchild)+tree.valed
    else:
        return False # Binary Tree Is Empty

# Return max depth of binary tree
def maxdepth(tree):
    if tree is None:
        return 0
    
    else :
        # Compute the depth of each subtree
        leftDepth = maxdepth(tree.leftchild)
        rightDepth = maxdepth(tree.rightchild)

        # Use the larger one
        if (leftDepth > rightDepth):
            return leftDepth+1
        else:
            return rightDepth+1

## Test Program ##                
root=BinaryTree(100)
root.insert(50)
root.insert(120)
root.insert(20)
root.insert(140)
root.delete(20)
print("PreOrder:")
root.preordrer()
print(end="\n")
print("InOrder:")
root.inorder()
print(end="\n")
print("PostOrder:")
root.postorder()
print(end="\n")
print("Count Of Nodes:",countofnodes(root))
print("Count Of Leaf Nodes:",countofleafnodes(root))
print("Sum Of Nodes:",sumofnodes(root))
print("Level of the binary tree:",maxdepth(root))

