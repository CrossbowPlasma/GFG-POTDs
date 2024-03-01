# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self, arr, n):
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Check if mid is a peak element
            if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
                return mid
            
            # If the element to the right of mid is greater, there must be a peak on the right side
            if mid < n - 1 and arr[mid] < arr[mid + 1]:
                left = mid + 1
            # Otherwise, there must be a peak on the left side
            else:
                right = mid
        
        # If there is only one element left, it must be a peak
        return left




#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends