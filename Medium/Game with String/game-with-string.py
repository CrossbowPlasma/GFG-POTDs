#User function Template for python3

from collections import Counter
import heapq

class Solution:
    def minValue(self, s, k):
        counter = Counter(s)
        
        counts = counter.values()
        counts = [-x for x in counts]
        heapq.heapify(counts)
        
        while k > 0:
            curItem = -heapq.heappop(counts)
            curItem -= 1
            k -= 1
            heapq.heappush(counts, -curItem)
        
        res = 0
        for count in counts:
            res += (-count) ** 2
        return res
        
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends