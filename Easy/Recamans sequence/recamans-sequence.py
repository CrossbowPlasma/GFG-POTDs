#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        a = [0] * (n + 1)
        st = set()
        for i in range(1, n + 1):
            if (a[i - 1] - i) > 0 and (a[i - 1] - i) not in st:
                a[i] = a[i - 1] - i
            else:
                a[i] = a[i - 1] + i
            st.add(a[i])
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends