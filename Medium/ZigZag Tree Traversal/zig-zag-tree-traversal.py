#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        # if the tree is empty, return an empty list
        if not root:
            return []
        
        # list to store the zig-zag level order traversal
        result = []
        
        # stack for the current level and next level
        current_level = []
        next_level = []
        
        # flag to determine the order of traversal (left to right or right to left)
        left_to_right = True
        
        # push the root node onto the current level stack
        current_level.append(root)
        
        # loop until the current level stack is empty
        while current_level:
            # pop the node from the current level stack
            node = current_level.pop()
            
            # add the node value to the result list
            result.append(node.data)
            
            # if the traversal is from left to right, push the left child first
            # and then the right child onto the next level stack
            if left_to_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # if the traversal is from right to left, push the right child first
            # and then the left child onto the next level stack
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
            
            # if the current level stack is empty, swap the current level stack
            # with the next level stack and toggle the flag for traversal direction
            if not current_level:
                current_level, next_level = next_level, current_level
                left_to_right = not left_to_right
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

from collections import defaultdict
from collections import deque

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.zigZagTraversal(root)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends