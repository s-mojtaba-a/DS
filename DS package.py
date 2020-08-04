# A package including BST and LinkedList
# LinkedList
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    
class linckedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    # inserting a value to the tail of your linkedlist 
    def insert(self,val):
        ''' give me a value to insert it to the tail of your linkedlist '''
        if not self.head :
            self.head=node(val)
            self.tail=self.head
        else:
            y=node(val)
            self.tail.next=y
            y.prev=self.tail
            self.tail=y
    # a method to delete the first node with the value = val
    def delete(self,val):
        ''' give me the value which you want to delete
            this method deletes the first node with the value = val '''
        # finding the first node with data = val
        x=x.head
        while x.data!=val :
            x=x.next
        # deleting the node 
        if x!=x.head and x!=x.tail :
            x.next.prev=x.prev
            x.prev.next=x.next
        elif x==self.head:
            x.next.prev=None
            self.head=x.next
        elif x==x.tail and x.data==self.tail.data:
            x.prev.next=None
            self.tail=x.prev
        else:
            raise Exception ('{} did not found'.format(val))

    # a method to find the k th element of your linkedlist
    def find(self,k):
        ''' give a k in range ( 1 , lenght of your linkedlist )
            this method will return the k th element of your linkedlist'''
        x=x.head
        if k==0:
            raise Exception ('k is out of range')
        while k>1:
            try:
                x=x.next
                k-=1
            except AttributeError:
                raise Exception ('k is out of range')
        if not x:
            raise Exception ('k is out of range')
        else:
            return(x.data)

    # a method to find the lenght of your linkedlist
    def lenght(self):
        ''' this method will return the lenght of your linkedlist '''
        k=1
        x=self.head
        while x!=self.tail:
            x=x.next
            k+=1
        return k
    # a method to delete the k th element of the list
    def dell(self,k):
        ''' give a number in range ( 1 , lenght of your linkedlist ) '''
        x=x.head
        if k==0:
            raise Exception ('k is out of range')
        if k>self.lenght():
            raise Exception ('k is out of range')
        # finding the k th node
        while k>1:
            x=x.next()
            k-=1
        # deleting the k th node
        if x!=x.head and x!=x.tail :
            x.next.prev=x.prev
            x.prev.next=x.next
        elif x==self.head:
            x.next.prev=None
            self.head=x.next
        elif x==x.tail and x.data==self.tail.data:
            x.prev.next=None
            self.tail=x.prev
    
    # a method to print the linklist from head to tail
    def printt(self):
        ''' it will print the linkedlist from head to tail '''
        x=self.head
        while x:
            print(x.data.end=' ')
            x=x.next
    
    
