class DoctorNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, new_name, side):
        parent = self.find_doctor(self.root, parent_name)

        if parent is None:
             return False

        if side == "left":
             parent.left = DoctorNode(new_name)

        elif side == "right":
            parent.right = DoctorNode(new_name)

        else:
             return False

        return True

    def find_doctor(self,node,name):
         if node is None:
              return None
         
         if node.value ==name:
              return node

         found = self.find_doctor(node.left, name)

         if found is not None:
              return found

         return self.find_doctor(node.right, name)
    

    def preorder(self, node=None):
            if node is None:
                return []
            result = [node.value]

            result += self.preorder(node.left)
            result += self.preorder(node.right)

            return result

    def inorder(self, node):
        if node is None:
            return []
        result = []
        result += self.inorder(node.left)
        result.append(node.value)
        result += self.inorder(node.right)

        return result

    def postorder(self,node):
        if node is None:
            return []
        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.value)

        return result









# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right")
tree.insert("Dr. Phan", "Dr. Morgan", "left")


print(tree.preorder(tree.root))
print(tree.inorder(tree.root))
print(tree.postorder(tree.root))

print(tree.insert("Dr. Dune", "Dr. Pan", "left"))
print(tree.insert("Dr Croft", "Dr. Pan", "middle"))


