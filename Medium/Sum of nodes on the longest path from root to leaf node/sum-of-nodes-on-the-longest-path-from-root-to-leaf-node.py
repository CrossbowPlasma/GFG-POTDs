#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def longestPathUtil(self, root):
        if not root:
            return (0, 0)  # Return (length, sum) for an empty tree
        
        # Recursively find the longest path and sum for left and right subtrees
        left_length, left_sum = self.longestPathUtil(root.left)
        right_length, right_sum = self.longestPathUtil(root.right)
        
        # Compare the lengths of left and right subtrees
        if left_length > right_length:
            max_length = left_length + 1
            max_sum = left_sum + root.data
        elif right_length > left_length:
            max_length = right_length + 1
            max_sum = right_sum + root.data
        else:
            # If lengths are equal, choose the path with maximum sum
            max_length = left_length + 1
            max_sum = max(left_sum, right_sum) + root.data
        
        return (max_length, max_sum)
    
    def sumOfLongRootToLeafPath(self, root):
        # Call the utility function to find the longest path and sum
        _, max_sum = self.longestPathUtil(root)
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
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
    test_cases = int(input())
    for cases in range(test_cases):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.sumOfLongRootToLeafPath(root)
        print(res)
# } Driver Code Ends