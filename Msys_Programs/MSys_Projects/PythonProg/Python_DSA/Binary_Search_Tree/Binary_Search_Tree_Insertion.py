# Binary search tree insertion using iterator function

class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self,element, left = None, right = None):
        self._element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self):
        self._root = None
    
    def rsearch(self, troot, key):
        if troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                return self.rsearch(troot._left, key)
            elif key > troot._element:
                return self.rsearch(troot._right, key)
        else:
            return False


    def search(self, key):
        troot = self._root
        while troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                troot = troot._left
            elif key > troot._element:
                troot = troot._left
        return False

    def delete(self, e):
        p = self._root
        pp = None
        while p and p._element != e:
            pp = p
            if e < p._element:
                p = p._left
            else:
                p = p._right
        if not p:
            return False
        if p._left and p._right:
            s = p._left
            ps = p
            while s._right:
                ps = s
                s = s._right
            p._element = s._element
            p = s
            pp = ps
        c = None
        if p._left:
            c = p._left
        else:
            c = p._right
        if p == self._root:
            self._root = None
        else:
            if p == pp._left:
                pp._left = c
            else:
                pp._right = c
            


    def rinsert(self,troot,e):
        if troot:
            if e < troot._element:
                troot._left = self.rinsert(troot._left, e)
            elif e > troot._element:
                troot._right = self.rinsert(troot._right, e)
        else:
            n = _Node(e)
            troot = n
        return troot

    def insert(self,troot,e):
        temp = None
        while troot:
            temp = troot
            if e == troot._element:
                return
            elif e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
        n = _Node(e)
        if self._root:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n

        else:
            self._root = n
    
    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=" ")
            self.inorder(troot._right)
            
    def preorder(self,troot):
        if troot:
            print(troot._element, end=" ")
            self.preorder(troot._left)
            self.preorder(troot._right)
    
    def postorder(self,troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end=" ")

B = BinarySearchTree()
# B.insert(B._root,50)
# B.insert(B._root,20)
# B.insert(B._root,30)
# B.insert(B._root,60)
# B.insert(B._root,10)
B._root = B.rinsert(B._root,50)
B.rinsert(B._root,30)
B.rinsert(B._root,80)
B.rinsert(B._root,10)
B.rinsert(B._root,40)
B.rinsert(B._root,60)
B.inorder(B._root)
print()
B.preorder(B._root)
print()
B.postorder(B._root)
print()
print(B.search(90))
print(B.rsearch(B._root,90))
print()
B.delete(80)
B.inorder(B._root)
