#User function Template for python3

class Solution:
     def DivisibleByEight(self,s):
        #code here
        r = 0
        for e in s:
            r = r*10+ord(e)-ord('0')
            r = r%8
        return 1 if r == 0 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends