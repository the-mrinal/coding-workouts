class Solution:
    def letterCombinations(self, s: str) -> List[str]:
        if not s:
            return ""
        keyMap = {
            2: ['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
            }

        def recursion(s):
            if len(s) == 1:
                return keyMap[int(s[0])]

            res = recursion(s[1:])	
            curr_len  = len(res)
            new_res = []
            for k in keyMap[int(s[0])]:
                for i in range(curr_len):
                    new_res.append(k+res[i])

            return new_res
        
        return recursion(s)