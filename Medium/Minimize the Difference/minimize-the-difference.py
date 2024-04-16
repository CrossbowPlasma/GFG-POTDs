
from typing import List


class Solution:
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        pre,suf=[],[]
        mi,ma=arr[0],arr[0]
        for i in range(n-k):
            mi=min(mi,arr[i])
            ma=max(ma,arr[i])
            pre.append([mi,ma])
        
        mi,ma=arr[-1],arr[-1]
        for i in range(n-1,k-1,-1):
            mi=min(mi,arr[i])
            ma=max(ma,arr[i])
            suf.append([mi,ma])
        suf=suf[::-1]
        # print(pre,suf)
        i,j=-1,0
        ans=float("inf")
        while(j<=n-k):
            if(i==-1):
                dif=suf[j][1]-suf[j][0]
                ans=min(ans,dif)
            elif(j==n-k):
                dif=pre[i][1]-pre[i][0]
                ans=min(ans,dif)
            else:
                p,s=pre[i],suf[j]
                dif=max(p[1],s[1])-min(p[0],s[0])
                ans=min(ans,dif)
            i+=1
            j+=1
        return(ans)
        



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
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.minimizeDifference(n, k, arr)
        
        print(res)
        

# } Driver Code Ends