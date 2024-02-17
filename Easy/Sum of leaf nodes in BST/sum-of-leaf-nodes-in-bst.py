#User function Template for python3

##Structure of node
'''
class Node:
    def __init__(self, data=0):
        self.data=0
        self.left=None
        self.right=None
'''

class Solution:
    def sumOfLeafNodes(self, root):
        if root is None:
            return 0
        
        # Initialize the sum
        leaf_sum = 0
        
        # Helper function to perform DFS
        def dfs(node):
            nonlocal leaf_sum
            if node is None:
                return
            
            # If node is a leaf node, add its value to the sum
            if node.left is None and node.right is None:
                leaf_sum += node.data
            
            # Recursively traverse left and right subtrees
            dfs(node.left)
            dfs(node.right)
        
        # Start DFS from the root
        dfs(root)
        
        return leaf_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data=0):
        self.data=data
        self.left=None
        self.right=None


def createNewNode(value):
    temp=Node()
    temp.data=value
    temp.left=None
    temp.right=None
    return temp
    

def newNode(root,data):
    if(root is None):
        root=createNewNode(data)
    elif(data<root.data):
        root.left=newNode(root.left,data);
    else:
        root.right=newNode(root.right,data)
        
    return root

for _ in range(int(input())):
    root=None
    sizeOfArray=int(input())
    arr=[int(x) for x in input().strip().split()]
    for i in arr:
        root=newNode(root,i)
    ob = Solution()
    print(ob.sumOfLeafNodes(root))
# } Driver Code Ends