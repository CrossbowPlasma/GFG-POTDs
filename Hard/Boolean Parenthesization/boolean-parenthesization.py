#User function Template for python3

class Solution:
    def countWays(self, n, s):
        MOD = 1003
        
        def countParentheses(symbols, operators):
            n = len(symbols)
            dp_true = [[0] * n for _ in range(n)]
            dp_false = [[0] * n for _ in range(n)]
            
            for i in range(n):
                if symbols[i] == 'T':
                    dp_true[i][i] = 1
                else:
                    dp_false[i][i] = 1
            
            for gap in range(1, n):
                for i in range(n - gap):
                    j = i + gap
                    for k in range(i, j):
                        if operators[k] == '&':
                            dp_true[i][j] += dp_true[i][k] * dp_true[k+1][j]
                            dp_false[i][j] += (dp_false[i][k] * dp_false[k+1][j] + 
                                               dp_false[i][k] * dp_true[k+1][j] + 
                                               dp_true[i][k] * dp_false[k+1][j])
                        elif operators[k] == '|':
                            dp_true[i][j] += (dp_true[i][k] * dp_true[k+1][j] +
                                              dp_true[i][k] * dp_false[k+1][j] +
                                              dp_false[i][k] * dp_true[k+1][j])
                            dp_false[i][j] += dp_false[i][k] * dp_false[k+1][j]
                        elif operators[k] == '^':
                            dp_true[i][j] += (dp_true[i][k] * dp_false[k+1][j] +
                                              dp_false[i][k] * dp_true[k+1][j])
                            dp_false[i][j] += (dp_true[i][k] * dp_true[k+1][j] +
                                               dp_false[i][k] * dp_false[k+1][j])
                        dp_true[i][j] %= MOD
                        dp_false[i][j] %= MOD
            
            return dp_true[0][n-1]
        
        symbols = []
        operators = []
        for char in s:
            if char in ('T', 'F'):
                symbols.append(char)
            else:
                operators.append(char)
        
        return countParentheses(symbols, operators)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends