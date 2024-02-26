#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
        res = ['']
        for a in s:
            res = res + [x + a for x in res]
        return sorted(res[1:])


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends