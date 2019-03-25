class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else:
            lastNode=self.head
            while lastNode.next != None:
                lastNode=lastNode.next
            lastNode.next=newNode
    def prepend(self, data): 
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        else:
            newNode.next=self.head
            self.head=newNode
    def insertAfterNode(self,prevNode,data):
        newNode=Node(data)
        newNode.next=prevNode.next
        prevNode.next=newNode
    def printList(self):
        curNode=self.head
        while curNode!= None:
            print(curNode.data)
            curNode=curNode.next
    def deleteNode(self, key):
        curNode=self.head
        if curNode!=None and curNode.data==key:
            self.head=curNode.next
            curNode=None
            return
        else:
            prev=None
            while curNode != None and curNode.data != key:
                prev=curNode
                curNode=curNode.next
            if curNode==None:
                print('The data is not found in the list')
                return
            else:
                prev.next=curNode.next
                curNode=None
                
    def deleteAtPos(self,pos):
        curNode=self.head
        if pos==0:
            self.head= curNode.next
            curNode=None
            return
        else:
            cnt=0
            prev=None
            while curNode != None and cnt != pos:
                prev=curNode
                curNode=curNode.next
                cnt+=1
            if curNode==None:
                print("The node doesn't exist")
                return
            else:
                prev.next=curNode.next
                curNode=None
            
    def len_iterative(self):
        cnt=0
        curNode=self.head
        while curNode != None:
            curNode=curNode.next
            cnt+=1
        return cnt

    def len_recursive(self,headNode):
        if headNode is None:
            return 0
        else:
            return 1+self.len_recursive(headNode.next)

    def swapNode(self,key1,key2):
        if key1==key2:
            print('The two nodes are the same nodes, cannot be swapped')
            return
        else:
            prev1=None
            curNode1=self.head
            while curNode1 != None and curNode1.data != key1:
                prev1=curNode1
                curNode1=curNode1.next
            prev2=None
            curNode2=self.head
            while curNode2 != None and curNode2.data != key2:
                prev2=curNode2
                curNode2=curNode2.next
            if curNode1==None or curNode2==None:
                print("The nodes don't exist in the list")
                return
    
            else:
                if prev1==None:
                    self.head=curNode2
                    prev2.next=curNode1
                elif prev2==None:
                    self.head=curNode1
                    prev1.next=curNode2
                else:
                    prev1.next=curNode2
                    prev2.next=curNode1
                temp1=curNode1.next
                temp2=curNode2.next
                curNode1.next=temp2
                curNode2.next=temp1
        
    def reverse_iterative(self):
        prev=None
        curNode=self.head
        while curNode!=None:
             nxt_temp=curNode.next
             curNode.next=prev
             prev=curNode
             curNode=nxt_temp
        self.head=prev
    
lst=linkedList()
lst.append('A')
lst.append('B')
lst.append('C')
lst.prepend('D')
lst.printList()
lst.deleteNode('A')
lst.deleteAtPos(0)
lst.printList()
print(lst.len_iterative())
print(lst.len_recursive(lst.head))
lst.swapNode('B','C')
lst.swapNode('B','B')
lst.reverse_iterative()
lst.printList()