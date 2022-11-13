
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
