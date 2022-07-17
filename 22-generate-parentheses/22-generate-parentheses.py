class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(S,left,right):
            if len(S) == n*2:
                ans.append(''.join(S))
                return 
            if left < n:
                S.append('(')
                generate(S,left + 1,right)
                S.pop()
            if right < left:
                S.append(')')
                generate(S,left,right + 1)
                S.pop()
        generate([],0,0)
        return ans
            