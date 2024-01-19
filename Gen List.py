class Node:
    def __init__(self,tag,data):
       self.tag=tag
       self.data=data
       self.link=None

class Genlist:
    def __init__(self):
        self.first=None
    
    # Insert data to gen list    
    def insert(self,tag,data):
        newnode=Node(tag,data) 
        if self.first is None:
            self.first=newnode # if list is empty
            return
        else:
            newnode.link=self.first
            self.first=newnode  
    
    # Print the gen list    
    def print(self):
        cur=self.first
        while(cur):
            print(cur.data,end="->")
            cur=cur.link
    
    # Print sum of the gen list
    def sum(self):
        s=0
        cur=self.first
        while(cur):
            s+=cur.data
            cur=cur.link
        return s
    
    # Find data in gen list
    def find(self,data):
        while(self.first):
            if self.first.data==data:
                self.first.data=5  # forexample change data to 5
                return self.first
            else:
                self.first=self.first.link
    
# Cheak equality of two gen list
def Equality(glist1:Genlist,glist2:Genlist):
    while glist1 and glist2:
        if(bool(glist1.first.tag)==bool(glist2.first.tag)):
            return True
        else:
            return False 
            
            
            
## Test Program ##
list=Genlist()
list1=Genlist()
list.insert(0,10)
list.insert(0,20)
list.insert(0,30)
list1.insert(0,10)
list1.insert(0,20)
list1.insert(1,30)
list.print()
print("\n")
list1.print()
print("\n")
print("Sum Of the Genlist is:",list.sum())
print(Equality(list,list1))

