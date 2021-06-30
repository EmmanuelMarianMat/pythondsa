import sys
class node:
    def __init__(self, value) -> None:
        self.data = value
        self.left = None
        self.right = None

class tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self,value):
        self.root = self.__insertHelper(self.root,value)

    def printTree(self):
        self.__printHelper(self.root)
        print()

    def getNodeCount(self):
        return self.__getCountHelper(self.root)

    def search(self,value):
        return self.__searchHelper(self.root,value) is not None

    def delete(self):
        self.__deleteHelper(self.root)
        self.root = None

    def successor(self,value):
        succ = self.__successorHelper(value)
        return succ.data if succ else -sys.maxsize 

    def deleteNode(self,value):
        self.root = self.__deleteNodeHelper(value,self.root)

    def BSTCheck(self):
        return self.__BSTCheckHelper(self.root)

    def __BSTCheckHelper(self,tree):
        if tree is None:
            return True
        if tree.left and tree.right:
            return self.__BSTCheckHelper(tree.left) and self.__BSTCheckHelper(tree.right) if tree.left.data<tree.data<=tree.right.data else False
        elif tree.left:
            return self.__BSTCheckHelper(tree.left) if tree.left.data<tree.data else False
        elif tree.right:
            return self.__BSTCheckHelper(tree.right) if tree.right.data>=tree.data else False
        else:
            return True
            


    def __deleteNodeHelper(self,value,tree):
        if tree is None:
            return None

        elif tree.data == value:
            if tree.left and tree.right:
                tree.data = self.__minHelper(tree.right).data
                tree.right = self.__deleteNodeHelper(tree.data,tree.right)
            else:
                return tree.left if tree.left else tree.right

        elif value<tree.data:
            tree.left = self.__deleteNodeHelper(value,tree.left)

        else:
            tree.right = self.__deleteNodeHelper(value, tree.right)

        return tree


    def __successorHelper(self, value):
        lastLeftTurn = None
        curr = self.root
        while curr:
            if curr.data == value:
                if curr.right:
                    return self.__minHelper(curr.right)
                return lastLeftTurn

            elif value<curr.data:
                lastLeftTurn = curr
                curr = curr.left
            else:
                curr = curr.right
        
        return None

    def min(self):
        return self.__minHelper(self.root).data

    def __minHelper(self,tre):
        if tre is None:
            return None
        curr = tre
        while(curr.left):
            curr = curr.left
        return curr

    def max(self):
        if self.root is None:
            return -sys.maxsize
        curr = self.root
        while(curr.right):
            curr = curr.right
        return curr.data

    def height(self,value):
        n = self.__searchHelper(self.root,value)
        return self.__heightHelper(n)

    def __heightHelper(self,tree):
        if tree is None:
            return 0
        return 1+max(self.__heightHelper(tree.left), self.__heightHelper(tree.right))

    def __deleteHelper(self,tree):
        if tree is None:
            pass
        elif tree.left is None and tree.right is None:
            del tree
        else:
            self.__deleteHelper(tree.left)
            self.__deleteHelper(tree.right)

    def __searchHelper(self,tree,value):
        if tree is None:
            return None
        if tree.data == value:
            return tree
        if value < tree.data:
            return self.__searchHelper(tree.left,value)
        else:
            return self.__searchHelper(tree.right,value)

    def __getCountHelper(self,tree):
        if tree is None:
            return 0
        return 1+self.__getCountHelper(tree.left)+self.__getCountHelper(tree.right)

    def __printHelper(self,tree):
        print('(',end="")
        if tree:
            print(tree.data,end="")
            self.__printHelper(tree.left)
            self.__printHelper(tree.right)
        print(')',end="")

    def __insertHelper(self,tree,value):
        if tree is None:
            return node(value)
        elif tree.data > value:
            tree.left = self.__insertHelper(tree.left,value)
        else:
            tree.right = self.__insertHelper(tree.right,value)

        return tree

def main():
    t = tree()
    t.insert(43)
    t.insert(15)
    t.insert(8)
    t.insert(30)
    t.insert(20)
    t.insert(35)
    t.insert(60)
    t.insert(50)
    t.insert(82)
    t.insert(70)
    t.printTree()
    print(t.getNodeCount())
    print(t.min(),t.max())
    for num in [43,15,8,30,20,35,60,50,82,70,42,83]:
        print(t.successor(num), end=" ")
    print()
    print(t.BSTCheck())
    t.deleteNode(82)
    print(t.BSTCheck())
    t.printTree()
    t._tree__minHelper(t.root).right = node(-sys.maxsize) # not binary tree
    t.printTree()
    print(t.BSTCheck())
    n = t._tree__minHelper(t.root).right
    t._tree__minHelper(t.root).right = None # binary tree again
    del n
    print(t.BSTCheck())

    for num in [43,15,8,30,20,35,60,50,82,70,42,83]:
        print(t.search(num), end=" ")
    print()

    for num in [43,15,8,30,20,35,60,50,82,70,42,83]:
        print(t.height(num), end=" ")
    print()
    
main()