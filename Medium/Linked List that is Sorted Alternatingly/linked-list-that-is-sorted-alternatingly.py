class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution:
    def sort(self, h1):
        s, d = Node(0), Node(0)
        w = s
        while h1:
            w.next = h1
            w = w.next
            h1, w.next = h1.next, None
            if h1:
                t = h1.next
                h1.next = d.next
                d.next = h1
                h1 = t
        w.next = d.next
        return s.next



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
        
        ob = Solution()
        resHead=ob.sort(ll1.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends