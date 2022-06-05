# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         if not text1 or not text2:
#             return ""
        
#         len1 = len(text1)
#         len2 = len(text2)
        
        
#         def dp(index1,index2):
#             if index1 == len1 or index2 == len2:
#                     return 0
                
            
#             if text1[index1] == text2[index2]:
#                     return 1 + dp(index1 + 1,index2 + 1)
#             else:
#                     return max(dp(index1 + 1,index2),dp(index1, index2 + 1))
#         return dp(0,0)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1 = len(text1)
        t2 = len(text2)
        dp = [[0]* (t2 +1) for _ in range(t1+1)]
        
        for index1 in range(t1-1,-1,-1):
            for index2 in range(t2-1,-1,-1):
                if text1[index1] == text2[index2]:
                    dp[index1][index2] = 1 + dp[index1 + 1][index2 + 1]
                else:
                    dp[index1][index2] = max(dp[index1+1][index2],dp[index1][index2 +1])
        
        return dp[0][0]