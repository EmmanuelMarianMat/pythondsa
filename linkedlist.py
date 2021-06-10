#%%
class node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
    
class llist:
    def __init__(self) -> None:
        self.head = None

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
        self.head = new

    def popFront(self):
        if self.empty():
            return None
        ret = self.head.val
        d = self.head
        self.head = self.head.next
        del d
        return ret

    def pushBack(self,value):
        new = node(value)
        if(self.empty()):
            self.head = new
            return
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = new

    def popBack(self):
        if self.empty():
            return None

        curr = self.head
        prev = None

        while curr.next:
            prev = curr
            curr = curr.next
        
        if prev==None:
            self.head = None
        else:
            prev.next = None

        ret = curr.val
        del curr
        return ret

    def front(self):
        if self.empty():
            return None
        return self.head.val

    def back(self):
        if self.empty():
            return None
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.val

        
    def insert(self,value,index):
        if index>self.size():
            return
        new = node(value)
        curr = self.head
        prev = None
        for i in range(index):
            prev = curr
            curr = curr.next

        if prev:
            prev.next = new
        else:
            self.head = new

        new.next = curr

    def erase(self,index):
        if index>=self.size():
            return
        curr = self.head
        prev = None
        for i in range(index):
            prev = curr
            curr = curr.next
            
        if prev:
            prev.next = curr.next
        else:
            self.head = self.head.next

        del curr

    def valueNFromEnd(self,n):
        siz = self.size()
        if n>=siz:
            return None
        return self.valueAt(siz-1-n)

    def reverse(self):
        prev,curr,next = None,self.head,None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def removeValue(self,value):
        prev,curr = None,self.head
        while curr:
            if curr.val==value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = self.head.next
                return
            prev = curr
            curr = curr.next
        
        if curr:
            del curr

    def printList(self):
        curr = self.head
        while curr!=None:
            print(f"{curr.val}",end=" -> ")
            curr=curr.next
        print("None")


l = llist()
l.reverse()
l.printList()
l.pushBack(6)
l.reverse()
l.printList()
l.pushFront(2)
l.reverse()
l.printList()
l.pushBack(3)
l.reverse()
l.printList()
l.pushFront(5)
l.reverse()
l.printList()
l.pushBack(1)
l.printList()
l.popFront()
l.popFront()
l.popFront()
l.popFront()
l.popFront()
for i in range(l.size()):
    print(l.valueAt(i),l.valueNFromEnd(i))
l.erase(0)
l.printList()
l.erase(4)
l.printList()
l.erase(3)
l.erase(1)
l.erase(1)
l.erase(0)
l.printList()

# %%
