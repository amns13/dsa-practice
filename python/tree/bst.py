class BSTNode:
    def __init__(self, data):
        self.data = data
        self.lc = None
        self.rc = None
        
    def search_bst(self, key):
        if not self:
            return None
        if key < self.data:
            return self.lc.search_bst(key)
        if key > self.data:
            return self.rc.search_bst(key)
        return self
    
    def _successor(self):
        if not self.rc:
            return None
        
        cur = self.rc
        while cur.lc:
            cur = cur.lc
        return cur
    
    def insert_bst_node(self, key):
        if key < self.data:
            if not self.lc:
                self.lc = BSTNode(data=key)
                return
            self.lc.insert_bst_node(key)
        elif key > self.data:
            if not self.rc:
                self.rc = BSTNode(data=key)
                return
            self.rc.insert_bst_node(key)
        else:
            raise KeyError(f"Key {key} already exists in BST.")
        
    def delete_value(self, key):
        if key == self.data:
            if not (self.rc or self.lc):
                return None
            elif not self.rc:
                return self.lc
            elif not self.lc:
                return self.rc
            else:
                successor = self._successor()
                successor.data, self.data = self.data, successor.data
                self.rc = self.rc.delete_value(key)
                return self
        elif key < self.data:
            if not self.lc:
                raise KeyError(f"Key {key} not found in bst")
            else:
                self.lc = self.lc.delete_value(key)
        else:
            if not self.rc:
                raise KeyError(f"Key {key} not found in bst")
            else:
                self.rc = self.rc.delete_value(key)
        
        return self
                
    @classmethod
    def inorder(cls, root):
        if root:
            cls.inorder(root.lc)
            print(root.data, end=' ')
            cls.inorder(root.rc)

    @classmethod
    def preorder(cls, root):
        if root:
            print(root.data, end=' ')
            cls.preorder(root.lc)
            cls.preorder(root.rc)
    
    @classmethod
    def postorder(cls, root):
        if root:
            cls.postorder(root.lc)
            cls.postorder(root.rc)
            print(root.data, end=' ')

    @classmethod
    def display(cls, root):
        traversals = {"Inorder": cls.inorder,
                      "Preorder": cls.preorder,
                      "Postorder": cls.postorder}
        for traversal_name, traversal_func in traversals.items():
            print(traversal_name)
            traversal_func(root)
            print()


if __name__ == "__main__":
    root = BSTNode(10)
    root.insert_bst_node(5)
    root.insert_bst_node(7)
    root.insert_bst_node(2)
    root.insert_bst_node(3)
    root.insert_bst_node(1)
    root.insert_bst_node(8)
    root.insert_bst_node(6)
    root.insert_bst_node(12)
    root.insert_bst_node(13)
    root.insert_bst_node(11)
    root.insert_bst_node(18)
    root.insert_bst_node(16)
    
    BSTNode.display(root)
    
    print("********************  DELETING 1  ******************")
    root = root.delete_value(1)
    BSTNode.display(root)
    
    print("********************  DELETING 18  ******************")
    root = root.delete_value(18)
    BSTNode.display(root)
    
    print("********************  DELETING 5  ******************")
    root = root.delete_value(5)
    BSTNode.display(root)
    
    print("********************  DELETING 10  ******************")
    root = root.delete_value(10)
    BSTNode.display(root)
    
    
    new_root = BSTNode(5)
    BSTNode.display(new_root)
    new_root = new_root.delete_value(5)
    BSTNode.display(new_root)
    