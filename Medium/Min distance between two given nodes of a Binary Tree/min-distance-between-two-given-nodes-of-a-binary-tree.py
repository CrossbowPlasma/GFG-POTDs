#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findDist(self, root, a, b):
        # Helper function to find the Lowest Common Ancestor (LCA)
        def findLCA(node, p, q):
            if not node:
                return None
            if node.data == p or node.data == q:
                return node
            left_lca = findLCA(node.left, p, q)
            right_lca = findLCA(node.right, p, q)
            if left_lca and right_lca:
                return node
            return left_lca if left_lca else right_lca

        # Helper function to find the distance between a node and a target
        def findDistance(node, target, dist):
            if not node:
                return float('inf')
            if node.data == target:
                return dist
            return min(findDistance(node.left, target, dist + 1), findDistance(node.right, target, dist + 1))

        # Find the LCA of the given nodes
        lca = findLCA(root, a, b)
        # Calculate the distance from the LCA to node 'a'
        dist_a = findDistance(lca, a, 0)
        # Calculate the distance from the LCA to node 'b'
        dist_b = findDistance(lca, b, 0)
        # Return the sum of distances between the LCA and both nodes
        return dist_a + dist_b


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

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


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        a, b=map(int, input().split())
        ob = Solution()
        print(ob.findDist(root, a, b))

# } Driver Code Ends