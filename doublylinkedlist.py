#%%
class node:
    def __init__(self,val) -> None:
        self.val = val
        self.prev = None
        self.next = None

class llist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def size(self):
        curr = self.head
        size=0
        while curr!=None:
            size+=1
            curr=curr.next
        return size

    def empty(self):
        return True if self.head == None else False

    def valueAt(self, index):
        if self.empty():
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def pushFront(self,value):
        new = node(value)
        new.next = self.head
        if self.empty():
            self.tail = new
        else:
            self.head.prev = new
        self.head = new

    def popFront(self):
        if self.empty():
            return None
        ret = self.head.val
        d = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        del d
        return ret

    def pushBack(self,value):
        new = node(value)
        new.prev = self.tail
        if self.empty():
            self.head = new
        else:
            self.tail.next = new
        
        self.tail = new

    def popBack(self):
        if self.empty():
            return None
        ret = self.tail.val
        d = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        
        del d
        return ret

    def front(self):
        if self.empty():
            return None
        return self.head.val

    def back(self):
        if self.empty():
            return None
        return self.tail.val

    def insert(self,value,index):
        if index>self.size():
            return

        new = node(value)
        if self.empty():
            self.head = new
            self.tail = new
            return
        
        curr = self.head
        prev = None
        for _ in range(index):
            prev = curr
            curr = curr.next

        new.next = curr
        new.prev = prev

        if curr:
            curr.prev = new
        else:
            self.tail.next = new
            self.tail = new

        if prev:
            prev.next = new
        else:
            self.head.prev = new
            self.head = new

    def erase(self,index):
        if index>=self.size():
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev
        
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        del curr

    def valueNFronEnd(self,n):
        siz = self.size()
        if n>=siz:
            return None
        return self.valueAt(siz-1-n)

    def reverse(self):
        curr = self.head
        while curr:
            curr.prev,curr.next = curr.next,curr.prev
            curr = curr.prev

        self.head,self.tail = self.tail,self.head

    def removeValue(self,value):
        curr = self.head
        while curr:
            if curr.val == value:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev

                del curr
                return
            curr = curr.next

    def printList(self):
        curr = self.head
        while curr!=None:
            print(f"{curr.val}",end=" -> ")
            curr=curr.next
        print("None")


l = llist()
# l.pushFront(5)
# l.printList()
# l.pushFront(6)
# l.printList()
# l.pushFront(7)
# l.printList()
# print(l.popBack(),l.popBack(),l.popBack(),l.popBack())
# l.pushBack(5)
# l.printList()
# l.pushBack(6)
# l.printList()
# l.pushBack(7)
# l.printList()
# print(l.popFront(),l.popFront(),l.popFront(),l.popFront())
l.reverse()
l.insert(5,1)
l.reverse()
l.printList()
l.reverse()
l.insert(5,0)
l.printList()
l.insert(6,2)
l.printList()
l.insert(6,0)
l.reverse()
l.printList()
l.insert(7,1)
l.reverse()
l.printList()
l.insert(8,3)
l.reverse()
l.printList()
l.popBack()
l.popBack()
l.popBack()
l.removeValue(8)
l.printList()
# %%
