class node:
    def __init__(self,key):
        self.key=key
        self.left=None 
        self.right=None 
class BST:
    def __init__(self):
        self.root=None 
    #insertion
    def insert (self,root,key):
        if root is None:
            return node(key)
        if key < root.key:
            root.left=self.insert(root.left,key) #recursive calling function
        else:
            root.right=self.insert(root.right,key)  #recursive calling function
        return root 
#inorder traversal (sorted order) printing the data in an order is called travels
    def inorder (self,root):
        if root:
            self.inorder(root.left) #left sub tree 
            print(root.key,end=" ")
            self.inorder(root.right) #right sub tree
    #search
    def search(self,root,key):
        if root is None or root.key==key: #comparition with root node
            return root 
        if key<root.key:
            return self.search(root.left,key)
        return self.search(root.right,key)

    #find minimum value node
    def minvalueNode(self,node): #when the children as 2 
        current=node
        while current.left is not None:
            current=current.left
        return current 

    #Deletion 
    def delete(self,root,key):
        if root is None:  #for root is present or not 
            return root  
        if key<root.key:
            root.left=self.delete(root.left,key) #search nleft side
        elif key>root.key:
            root.right= self.delete(root.right,key) #search right side
        else:
            #node with one child or no child
            if root.left is None:
                return root.right 
            elif root.right is None:
                return root.left 
            #node with 2 children 
            temp=self.minvalueNode(root.right)
            root.key=temp.key
            root.right=self.delete(root.right,temp.key)
        return root
    
    #----test the Bst implememtation----
tree= BST()
keys=[50,30,70,20,40,60,80]
for key in keys:
    tree.root=tree.insert(tree.root,key)
print("Inoder traversal of the BST: ")
tree.inorder(tree.root)
#search for a key 
key=60 
found=tree.search(tree.root,key)
print(f"\n\nsearch for {key}:","Found" if found else "Not Found")
print(f"\nSearch for {key}:","Found" if found else "Not Found")

#delete node
tree.root = tree.delete(tree.root, 20)
print("\nInorder after deleting 20:")
tree.inorder(tree.root)

tree.root = tree.delete(tree.root, 30)
print("\nInorder after deleting 30:")
tree.inorder(tree.root)

tree.root = tree.delete(tree.root, 50)
print("\nInorder after deleting 50:")
tree.inorder(tree.root)