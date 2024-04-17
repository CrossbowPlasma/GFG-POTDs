#User function Template for python3

class Solution:    
    def countPairs(self,arr, n): 
        def merge(arr, low, mid, high):
            left = low
            right = mid + 1
            count = 0
            ans = []
            
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    ans.append(arr[left])
                    left += 1
                else:
                    count += (mid - left + 1)
                    ans.append(arr[right])
                    right += 1
            
            while left <= mid:
                ans.append(arr[left])
                left += 1
            
            while right <= high:
                ans.append(arr[right])
                right += 1
            
            for i in range(low, high+1):
                arr[i] = ans[i - low]
            
            return count
            
        
        def merge_sort(arr, left, right):
            mid = (left + right) // 2
            count = 0
            if left < right:
                count += merge_sort(arr, left, mid)
                count += merge_sort(arr, mid+1, right)
                count += merge(arr, left, mid, right)
            return count
            
        for i in range(n):
            arr[i] *= i
        
        return merge_sort(arr, 0, n-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob= Solution()
        print(ob.countPairs(a, n))

        T -= 1


if __name__ == "__main__":
    main()
    
# } Driver Code Ends