class Solution:
    def matrixDiagonally(self, mat):
        n = len(mat)
        result = []

        i, j = 0, 0
        isUp = True

        for _ in range(n * n):
            result.append(mat[i][j])

            if isUp:
                if j == n - 1:
                    i += 1
                    isUp = False
                elif i == 0:
                    j += 1
                    isUp = False
                else:
                    i -= 1
                    j += 1
            else:
                if i == n - 1:
                    j += 1
                    isUp = True
                elif j == 0:
                    i += 1
                    isUp = True
                else:
                    i += 1
                    j -= 1

        return result


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends