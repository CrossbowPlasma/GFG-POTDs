#User function Template for python3
class Solution:
    def nthPosition(self, n):
        power_of_2 = 1
        while power_of_2 <= n:
            power_of_2 *= 2
        return power_of_2 // 2

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthPosition(n))
# } Driver Code Ends