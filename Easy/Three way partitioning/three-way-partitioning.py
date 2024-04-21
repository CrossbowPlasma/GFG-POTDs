#User function template for Python

class Solution:
    def threeWayPartition(self, array, a, b):
        f=[i for i in array if i<a ]
        m= [ i for i in array if i >=a and i <=b]
        l =[i for i in array if i > b ]
        #print(f, m, l)
        ans =[]
        for i in f :
            ans.append(i)
        #print(ans)
        for i in m :
            ans.append(i)
        #print(ans)
        for i in l :
            ans.append(i)
            
        #print(ans)
        for i in range(len(array)):
            array[i]= ans[i]


#{ 
 # Driver Code Starts
#Initial template for Python

from collections import Counter

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        original = Counter(array)
        a,b = list(map(int, input().strip().split()))
        ob = Solution()
        ob.threeWayPartition(array, a, b)

        k1 = k2 = k3 = 0
        for e in array:
            if e > a:
                k3+=1
            elif e<=a and e>=b:
                k2+=1
            elif e<a:
                k1+=1

        m1 = m2 = m3 = 0
        for e in range(k1):
            if array[e]<a:
                m1+=1
        for e in range(k1, k1+k2):
            if array[e]<=a and array[e]>=b:
                m2+=1
        for e in range(k1+k2, k1+k2+k3):
            if array[e]>=a:
                m3+=1

        flag = False
        if k1==m1 and k2==m2 and k3==m3:
            flag = True
        for e in range(len(array)):
            original[array[e]]-=1
        for e in range(len(array)):
            if original[array[e]]!=0:
                flag = False
        if flag:
            print(1)
        else:
            print(0)

# } Driver Code Ends