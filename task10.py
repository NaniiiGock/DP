
from math import inf
class Solution:
    def minCut(self,s: str) -> int:
        result = [i for i in range(-1,len(s))]
        for start in range(len(s)):
            for finish in range(start, len(s)):
                if s[start:finish] == s[finish:start:-1]:
                    #if part is palindrome
                    if result[finish+1] > result[start] +1:
                        result[finish+1] = result[start]+1
                        #change to lower number of slices
        return result[-1]

    
    def solve(s):
    lenn = len(s)
    cuts = [i for i in range(lenn)]
    matrix = [[False for j in range(lenn)] for j in range(lenn)] 
    for i in range(0,lenn):
        for j in range(0, i+1):
            if s[i] == s[j] and (i <= j+1 or matrix[j+1][i-1]):
                matrix[j][i] = True
                if j != 0:
                    cuts[i] = min(cuts[i], cuts[j-1]+1)
                else:
                    cuts[i] = 0
    return cuts[-1]
