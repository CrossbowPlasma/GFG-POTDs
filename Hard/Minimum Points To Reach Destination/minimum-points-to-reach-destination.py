class Solution:
    def minPoints(self, m, n, points):
        # Initialize dp array with zeros
        dp = [[0] * n for _ in range(m)]
        
        # Start from the destination cell
        dp[m-1][n-1] = max(1, 1 - points[m-1][n-1])
        
        # Fill dp array from bottom-right to top-left
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # Skip the destination cell
                if i == m-1 and j == n-1:
                    continue
                
                # Calculate minimum points required to reach the destination cell
                if i == m-1:
                    # If we can only move right
                    min_points_to_right = dp[i][j+1] - points[i][j]
                    dp[i][j] = max(1, min_points_to_right)
                elif j == n-1:
                    # If we can only move down
                    min_points_to_down = dp[i+1][j] - points[i][j]
                    dp[i][j] = max(1, min_points_to_down)
                else:
                    # If we can move both right and down
                    min_points_to_right = dp[i][j+1] - points[i][j]
                    min_points_to_down = dp[i+1][j] - points[i][j]
                    min_points_required = min(min_points_to_right, min_points_to_down)
                    dp[i][j] = max(1, min_points_required)
        
        return dp[0][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m,n = int(m),int(n)
		points = []
		for _ in range(m):
			temp = [int(x) for x in input().split()]
			points.append(temp)
		ob = Solution()
		ans = ob.minPoints(m,n,points)
		print(ans)




# } Driver Code Ends