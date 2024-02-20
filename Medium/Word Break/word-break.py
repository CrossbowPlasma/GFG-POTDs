#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Convert dictionary into a set for faster lookup
        word_set = set(dictionary)
        # Initialize memoization dictionary
        memo = {}
        
        def can_break(s):
            if s in memo:
                return memo[s]
            
            if s in word_set:
                memo[s] = True
                return True
            
            for i in range(1, len(s)):
                prefix = s[:i]
                if prefix in word_set and can_break(s[i:]):
                    memo[s] = True
                    return True
            
            memo[s] = False
            return False
        
        return 1 if can_break(s) else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends