#User function Template for python3

class Solution:
    def twoRepeated(self, arr, n):
        visited = set()
        ans = []
        for num in arr:
            if num in visited:
                ans.append(num)
            else:
                visited.add(num)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends