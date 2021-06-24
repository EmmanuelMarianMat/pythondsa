from math import inf
import random

class MyHashMap:
    def __init__(self):
        self.cap = 20
        self.table = [None]*self.cap

    
    def add(self,key,value):
        hashed_key = key%self.cap
        for _ in range(self.cap):
            if self.table[hashed_key]==None or self.table[hashed_key][0]==key:
                self.table[hashed_key] = (key,value)
                return
            else:
                hashed_key = (hashed_key+1)%self.cap

        print("Could not insert")
        

    def exists(self,key):
        hashed_key = key%self.cap
        for _ in range(self.cap):
            if self.table[hashed_key]==None:
                break
            elif self.table[hashed_key][0]==key:
                return True
            else:
                hashed_key = (hashed_key+1)%self.cap

        return False


    def get(self,key):
        hashed_key = key%self.cap
        for _ in range(self.cap):
            if self.table[hashed_key]==None:
                break
            elif self.table[hashed_key][0]==key:
                return self.table[hashed_key][1]
            else:
                hashed_key = (hashed_key+1)%self.cap

        return None

    def delete(self,key):
        hashed_key = key%self.cap
        for _ in range(self.cap):
            if self.table[hashed_key]==None:
                break
            elif self.table[hashed_key][0]==key:
                prev = hashed_key
                for i in range(1,self.cap):
                    curr = (hashed_key+i)%self.cap
                    
                    if self.table[curr] is None:
                        break
                
                    curr_hash = self.table[curr][0]%self.cap

                    if curr_hash<curr:
                        if prev>=curr_hash and curr>prev:
                            self.table[prev]=self.table[curr]
                            prev = curr
                    elif curr_hash>curr:
                        if (prev>=curr_hash or prev<curr):
                            self.table[prev]=self.table[curr]
                            prev = curr

                self.table[prev] = None
                return

                    
                
            else:
                hashed_key = (hashed_key+1)%self.cap

        print("No such key in the table to delete")



def main():
    my_dict = MyHashMap()
    # my_dict.add(3,4)
    # my_dict.add(23,5)
    # my_dict.add(3,8)
    # my_dict.add(33,6)
    # my_dict.add(13,7)
    # my_dict.delete(3)
    # my_dict.add(-11,-5)
    # my_dict.add(-43,4)
    # my_dict.add(-1,-1)
    # my_dict.add(-5,-2)
    # my_dict.add(43,4)
    # my_dict.add(1,-1)
    # my_dict.add(5,-2)
    # my_dict.add(6,-9)
    # my_dict.add(7,-8)
    # my_dict.add(-6,-9)
    # my_dict.add(63,-8)
    # my_dict.add(11,-5)
    # my_dict.add(-2,-1)
    # my_dict.add(-15,-2)
    # my_dict.add(-64,-9)
    # my_dict.add(-72,-8)
    # my_dict.add(111,-5)
    # my_dict.delete(112)
    # my_dict.deSlete(-64)
    
    keys = set()
    
    for _ in range(100): 
        key = random.randint(-100,100)
        my_dict.add(key,0)
        if sum(key is not None for key in my_dict.table)==20:
            break

    for tuple in my_dict.table:
        keys.add(tuple[0])
        if any(not my_dict.exists(key[0]) for key in my_dict.table):
            print('Error before delete - keys only')

    for _ in range(300):
        chce = random.randint(-100,100)
        if my_dict.exists(chce)^(chce in keys):
            print(chce,  my_dict.exists(chce), chce in keys, 'Error before delete - general')
    
    for _ in range(20):
        ch = random.choice(my_dict.table)
        if ch:
            my_dict.delete(ch[0])
        for tuple in my_dict.table:
            if tuple and not my_dict.exists(tuple[0]):
                print('Error after delete')


main()