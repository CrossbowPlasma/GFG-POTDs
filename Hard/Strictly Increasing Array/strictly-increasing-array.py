#User function Template for python3

import bisect
class Solution:
    def min_operations(self,nums):
        for i in range(len(nums)):
            nums[i] -= i
        
        lis = []
        for num in nums:
            pos = bisect.bisect_right(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num
                
        return len(nums) - len(lis)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.min_operations(nums)
		print(ans)
# } Driver Code Ends