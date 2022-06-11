class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1) 
        n = len(s2)
        l = len(s3)
        if m + n != l:
            return False
        
        
        table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i==0 and j==0:
                    table[i][j] = True
                elif i == 0:
                    table[i][j] = table[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    table[i][j] = table[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    table[i][j] = (table[i-1][j] and s1[i-1] == s3[i+j-1]) or (table[i][j-1] and s2[j-1] == s3[i+j-1])
            
        
        
        
        return table[m][n]
