#User function Template for python3
class Solution:
    def sumBitDifferences(self, arr, n):
        result = 0
        # Iterate through each bit position
        for i in range(32):  # Considering integer is 32-bit
            # Count the number of elements with this bit set
            count_set_bit = sum((num >> i) & 1 for num in arr)
            # Count the number of elements with this bit unset
            count_unset_bit = n - count_set_bit
            # Add the contribution of this bit position to the result
            result += count_set_bit * count_unset_bit * 2
        return result



#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends