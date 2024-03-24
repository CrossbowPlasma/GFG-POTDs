class Solution:
    def NBitBinary(self, n):
        result = []
        self.generate_valid_binaries(n, "", 0, 0, result)
        return result
    
    def generate_valid_binaries(self, n, prefix, ones, zeros, result):
        if len(prefix) == n:
            result.append(prefix)
            return
        
        if ones > zeros:
            self.generate_valid_binaries(n, prefix + "1", ones + 1, zeros, result)
            self.generate_valid_binaries(n, prefix + "0", ones, zeros + 1, result)
        else:
            self.generate_valid_binaries(n, prefix + "1", ones + 1, zeros, result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends