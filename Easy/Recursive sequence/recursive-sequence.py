#User function Template for python3

class Solution:
    def sequence(self, n):
        result = 0
        ctn = 1
        for i in range(1,n+1):
            product = 1
            for j in range(i):
                product *= ctn
                ctn += 1
            result += product
        if n < 7:
            return result
        else:
            return result % (10**9 + 7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends