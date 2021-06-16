from math import inf
class MyHashMap:
    def __init__(self):
        self.cap = 20
        self.table = [None]*self.cap

    
    def add(self,key,value):
        hashed_key = key%self.cap
        for _ in range(self.cap):
            if self.table[hashed_key]==None:
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
                self.table[hashed_key] = (inf,0)
                return
            else:
                hashed_key = (hashed_key+1)%self.cap

        print("No such key in the table to delete")



def main():
    my_dict = MyHashMap()
    my_dict.add(3,4)
    my_dict.add(23,5)
    my_dict.add(3,8)
    my_dict.add(33,6)
    my_dict.add(13,7)
    print(my_dict.exists(13))
    print(my_dict.exists(23))
    print(my_dict.exists(3))
    print(my_dict.exists(5))
    print(my_dict.exists(33))
    print(my_dict.exists(14))
    print(my_dict.get(13))
    print(my_dict.get(23))
    print(my_dict.get(3))
    print(my_dict.get(5))
    print(my_dict.get(33))
    print(my_dict.get(14))
    my_dict.delete(3)
    my_dict.add(43,4)
    my_dict.add(1,-1)
    my_dict.add(5,-2)
    my_dict.add(6,-9)
    my_dict.add(7,-8)
    my_dict.add(-11,-5)
    my_dict.add(-43,4)
    my_dict.add(-1,-1)
    my_dict.add(-5,-2)
    my_dict.add(-6,-9)
    my_dict.add(-7,-8)
    my_dict.add(11,-5)
    my_dict.add(-2,-1)
    my_dict.add(-15,-2)
    my_dict.add(-64,-9)
    my_dict.add(-72,-8)
    my_dict.add(111,-5)
    my_dict.delete(112)


main()