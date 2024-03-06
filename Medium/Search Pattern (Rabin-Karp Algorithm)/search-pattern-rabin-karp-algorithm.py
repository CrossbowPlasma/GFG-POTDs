#User function Template for python3

class Solution:
    def computeLPSArray(self, pattern):
        """
        Compute the Longest Prefix Suffix (LPS) array for the pattern.
        """
        length = len(pattern)
        lps = [0] * length
        i = 1
        length_of_prev_longest_prefix_suffix = 0

        while i < length:
            if pattern[i] == pattern[length_of_prev_longest_prefix_suffix]:
                length_of_prev_longest_prefix_suffix += 1
                lps[i] = length_of_prev_longest_prefix_suffix
                i += 1
            else:
                if length_of_prev_longest_prefix_suffix != 0:
                    length_of_prev_longest_prefix_suffix = lps[length_of_prev_longest_prefix_suffix - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, pattern, text):
        """
        Search for occurrences of the pattern in the text.
        """
        result = []
        M = len(pattern)
        N = len(text)
        lps = self.computeLPSArray(pattern)
        i = 0  # Index for text[]
        j = 0  # Index for pattern[]

        while i < N:
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == M:
                result.append(i - j + 1)
                j = lps[j - 1]

            # Mismatch after j matches
            elif i < N and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends