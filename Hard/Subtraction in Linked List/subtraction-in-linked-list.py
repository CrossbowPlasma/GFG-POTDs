#User function Template for python3

class Solution:
    def subLinkedList(self, h1, h2):
        # removing zeros
        while h1 is not None and h1.data == 0:
            h1 = h1.next

        while h2 is not None and h2.data == 0:
            h2 = h2.next

        # finding length of LL
        s1 = self.getLength(h1)
        s2 = self.getLength(h2)

        if s1 == 0 and s2 == 0:
            return Node(0)

        # making l1 list size largest.
        if s2 > s1:
            temp = h1
            h1 = h2
            h2 = temp  # swap the list

        if s1 == s2:
            curr1 = h1
            curr2 = h2
            while curr1.data == curr2.data:
                curr1 = curr1.next
                curr2 = curr2.next

                # if reached end => both ll are same
                if curr1 is None:
                    return Node(0)
            if curr2.data > curr1.data:
                temp = h1
                h1 = h2
                h2 = temp  # swap the list

        # reverse the list for subtraction
        h1 = self.reverse(h1)
        h2 = self.reverse(h2)
        ans = None
        while h1 is not None:
            n1 = h1.data
            n2 = 0
            if h2 is not None:
                n2 = h2.data

            if n1 < n2:
                if h1.next is not None:
                    h1.next.data -= 1
                n1 += 10

            # store the difference
            curr = Node(n1 - n2)
            curr.next = ans
            ans = curr

            h1 = h1.next
            if h2 is not None:
                h2 = h2.next

        # remove zeros from end;
        while ans is not None and ans.next is not None:
            if ans.data == 0:
                ans = ans.next
            else:
                break
        return ans

    def getLength(self, head):
        cnt = 0
        curr = head
        while curr is not None:
            cnt += 1
            curr = curr.next
        return cnt

    def reverse(self, head):
        prev = None
        curr = head
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end='')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        ob = Solution()
        res = ob.subLinkedList(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends