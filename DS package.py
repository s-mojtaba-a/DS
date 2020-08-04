# A package including BST and LinkedList
# LinkedList
class node:
    def __init__(self,data):
        self.data=data
        self.next=None  # points to the next node
        self.prev=None  # points to the previous node
    
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
            print(x.data,end=' ')
            x=x.next
    
################################

############# BST ############

# making the bst's node
class nodee:
    def __init__(self,data):
        self.data=data
        self.parent=None # points to the parent of a node
        self.l=None  # points to the left child
        self.r=None  # points to the right child

# making the bst class
class BST:
    def __init__(self):
        self.root=None  # the root of our tree
    # inserting a value to our tree   
    def insert(self,val):
        ''' inserts the value to the tree '''
        x=self.root
        y=nodee(val)
        while True:
            if x.data>= val :
                if x.l:
                    x=x.l
                else:
                    x.l=y
                    y.parent=x
                    break
            else:
                if x.r:
                    x=x.r
                else:
                    x.r=y
                    y.parent=x
                    break
    # searchs for a value and if the value is in tree , returns True and else returns False
    def is_in_tree(self,val):
        ''' if val in tree :
                returns True
            else:
                returns False 
        '''
        x=self.root
        while x.data!= val:
            if val>x.data:
                x=x.r
            else:
                x=x.l
            if not x:
                return False
        return True
    
    # a function to replace a nodde with it's child
    def _replace(self,nodde,child):
        if not nodde.parent:  # nodde is the root of the tree
            self.root=child
        elif nodde.parent.l==nodde: # nodde is the left child of it's parent
            nodde.parent.l=child
        else:                       # nodde is the right child of it's parent
            nodde.parent.r=child
        child.parent=nodde.parent   # changing the parent of child
    
    # deleting a node
    def delete(self,nodde):
        ''' deletes nodde from your tree '''
        if  not nodde.r:
            self._replace(nodde,nodde.l)
        elif not nodde.l :
            self._replace(nodde,nodde.r)
        else:
            x=node.l
            while  x.r :
                x=x.r
            nodde.data=x.data
            self.delete(x)

    # printing in-order traversal of the tree starting from node x
    def in_order(self,x=self.root):
        ''' it prints in-order traversal of the tree , starting from node x '''
        if not x:
            return
        self.in_order(x.l)
        print(x.data)
        self.in_order(x.r)
    
    # printing pre-order traversal of the tree starting from node x
    def pre_order(self,x=self.root):
        ''' it prints pre-order traversal of the tree , starting from node x '''
        if not x:
            return
        print(x.data)
        self.pre_order(x.l)
        self.pre_order(x.r)
    
    # printing post-order traversal of the tree starting from node x
    def post_order(self,x=self.root):
        ''' it prints post-order traversal of the tree , starting from node x '''
        if not x:
            return
        self.post_order(x.l)
        self.post_order(x.r)
        print(x.data)

    