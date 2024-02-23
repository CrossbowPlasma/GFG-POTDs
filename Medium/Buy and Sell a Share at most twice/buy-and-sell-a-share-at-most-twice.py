from typing import List


class Solution:
    def maxProfit(self, n: int, price: List[int]) -> int:
        if n <= 1:
            return 0

        # Create two arrays to store the maximum profit if only one transaction
        # is allowed up to that day, from left and right respectively.
        max_profit_left = [0] * n
        max_profit_right = [0] * n

        # Calculate maximum profit if only one transaction is allowed up to each day from left
        min_price = price[0]
        for i in range(1, n):
            min_price = min(min_price, price[i])
            max_profit_left[i] = max(max_profit_left[i-1], price[i] - min_price)

        # Calculate maximum profit if only one transaction is allowed up to each day from right
        max_price = price[n-1]
        for i in range(n-2, -1, -1):
            max_price = max(max_price, price[i])
            max_profit_right[i] = max(max_profit_right[i+1], max_price - price[i])

        # Find the maximum profit by combining the profits from left and right
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_profit_left[i] + max_profit_right[i])

        return max_profit
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends