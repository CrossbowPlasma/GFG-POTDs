class Solution:
	def countPairs(self, mat1, mat2, n, x):
		a=[j for i in mat1 for j in i]
		b=[j for i in mat2 for j in i]
		b=set(b)
		count=0
		for i in a:
		    if x-i in b:
		        count+=1
		return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends