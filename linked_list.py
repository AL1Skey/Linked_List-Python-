class Node:
    head=None
    _next=None
    prev=None
    def __init__(self,value):
        self.head=value

class Link_list:
    #To initialize, insert node on Linked_list.head
    
    capacity = 0 #Size of linked_list, it used in append,prepend,insert,delete,pop,rpop
    
    def __init__(self):
        self.head=None
        self.tail=None
    def isEmpty(self):
        if self.head==None:
            print(" The list is Empty")
        return self.head==None
    def size(self):
        return self.capacity

    """
    Insertion
    Method:
        linkPrepend()
        linkAppend()
        insert()
        
    linkAppend,linkPrepend:
        Time Complexity=O(1)
        Space Complexity=O(1)
    Insert
        Time Complexity=O(n/2)
        Space Complexity=O(n/2)
    How it works
    Append
        use tail to append to next node with next pointer inside the node,then reasign the tail with new node.
        if list had None Node,then it will add new node
    Prepend
        use head to reassign the node
        make new head and assign it as new head
        make new head pointing to old head
        if list had None Node,then it will add new node
    """
    def insert(self,value,index=0):
        """
        if(index<0):
            print("Index is lower than zero. Do you want to prepend?")
            return
        elif(index>self.capacity):
            print("Index is out of bound. The size is ",self.capacity)
            return
        elif(index>0 and index <= self.capacity):
            #Operation
            size = self.capacity
            mid = size//2
            if (size%2)!=0:#if odd
                mid+=1
            header = self.head
            count = 0

            #problem: if index>mid then the loop cant adapt with tail indexing
                #ex: if index is 7 with size of 10 then it will go to prev two time not three time
            if index>mid:
                header=self.tail
                count = mid
                
                #Problem:traversing list from tail,the index need to reverse
                # N = O(1), N-1 = O(2), N-K = O(K+1)
                #SOLVED
                for i in range(size,index,-1):#for i equal to size and decrement to index
                    if(i==mid):#if i is same as mid,then break
                        break
                    header=header.prev #traverse the linked list from tail                    
                    
            else:
                for i in range(count,index):#for i in range 0 to index 
                    header=header._next
                    print("head")
            
            new_node = Node(value)
            new_node.prev = header
            new_node._next = header._next

            header._next = new_node
            self.capacity+=1
            
        else:
            self.linkPrepend(value)
            print("Inserted in index ",index)
            return
        
        print("Inserted in index ",index)
        return
        """
        if self.isEmpty():
            return

        if index==0:
            self.linkPrepend(value)
            return
        elif index<0 or index>=self.capacity:
            print("Index is Out of bound")
            return
        
        node= self.peekNode(index)
        new_node = Node(value)
        new_node.prev = node
        new_node._next = node._next

        node._next = new_node
        self.capacity+=1
        
        
    def linkAppend(self,value):
        if self.isEmpty():
            self.head=Node(value)
            
        else:
            header = self.head
            if self.tail:
                header = self.tail
            new_node = Node(value)
            new_node.prev = header
            header._next = new_node
    
            self.tail = header._next      

        self.capacity += 1
        return
    def linkPrepend(self,value):
        if(self.head):
            new_node = Node(value)
            new_node._next = self.head
            self.head.prev = new_node
            self.head = new_node

            if(self.size()<2):
                self.tail = new_node._next
                
        else:
            self.head = Node(value)

        self.capacity += 1
        return

    """
    Removing
    Method:
        remove()
        pop()
        rpop()
    
    """
    def remove(self,index):
        if self.isEmpty():
            return
        
        nodes=self.peekNode(index)
        value=nodes.head

        #If nodes is not empty
        if nodes is self.head:
            self.rpop()
        elif nodes is self.tail:
            self.pop()
        else:
            prev_nodes=nodes.prev
            next_nodes=nodes._next

            prev_nodes._next = next_nodes
            next_nodes.prev = prev_nodes

        del nodes
        self.capacity -=1

        print("The nodes in index ",index," with value ",value,"removed successfully")
        print("New list : ",self.list())
        return
    def pop(self):
        if self.isEmpty():
            return
        #If isn't empty
        if self.tail:
            node=self.tail
            self.tail=node.prev
        elif self.head:
            node=self.head
            self.head=None
        del node
        self.capacity -=1
        print("Popped Successfully")
    def rpop(self):
        if self.isEmpty():
            return
        #If isn't empty
        if self.head:
            node=self.head
            self.head=node._next
        elif self.tail:
            node=self.tail
            self.tail=None
        del node
        self.capacity -=1
        print("Popped Successfully")
        
    def peekNode(self,index):
        """
        if ( (index >= self.size()) or (index < 0) ):
             print("Index out of bound")
             return
        else:
            header = self.head
            count = 0

            for i in range(0, index):
                print(i)
                header=header._next

            return header
        """
        
        if self.isEmpty():
            return
        
        size = self.capacity
        mid = size//2
        if (size%2)!=0:#if odd
            mid+=1
        header = self.head
        count = 0

        #problem: if index>mid then the loop cant adapt with tail indexing
            #ex: if index is 7 with size of 10 then it will go to prev two time not three time
        if index>mid:
            header=self.tail
            count = mid
            
            #Problem:traversing list from tail,the index need to reverse
            # N = O(1), N-1 = O(2), N-K = O(K+1)
            #SOLVED
            for i in range(size,index,-1):#for i equal to size and decrement to index
                if(i==mid):#if i is same as mid,then break
                    break
                header=header.prev #traverse the linked list from tail                    
        else:
            for i in range(count,index):#for i in range 0 to index 
                header=header._next
                #print("head")

        return header
        
        
    def peek(self,index):
        if ( (index > self.size()) or (index < 0) ):
             print("Index out of bound")
             return False
        else:
            return self.peekNode(index).head
        
    def find(self,value):
        header = self.head
        arrIndex = []
        count=0
        while header:
            if header.head==value:
                arrIndex.append(count)

            header=header._next
            count+=1
        if not arrIndex:# IF arrIndex is empty
            print("The value you search is not found in any index")
            return
        
        result=", ".join(map(str,arrIndex))
        print(" value you search are in index ",result)
        return arrIndex

    def list(self):
        if self.isEmpty():
            return
        header = self.head
        nodes=[]
        while header:
            if header is self.head:
                nodes.append("[Head: %s]->" % header.head)
            elif header._next is None:
                nodes.append("<-[Tail: %s]" % header.head)
            else:
                nodes.append("<-[ %s]->" % header.head)
            header=header._next

        return "".join(nodes)


node = Node(91)
link = Link_list()
for i in range(0,10):
    link.linkAppend(i)



    
                
            
