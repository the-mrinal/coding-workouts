class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z'],
        }
        
        '''
        23
        
        def
        
        ad,bd,cd,ae,be,ce bc
        
        '''
        n = len(digits)
        def combinationHelper(index):
            if index == n - 1:
                return letterMap[int(digits[index])]
            
            comb = combinationHelper(index + 1)
            size = len(comb)
            new_comb = []
            for i in range(size):
                for elem in letterMap[int(digits[index])]:
                    new_comb.append(elem + comb[i])
            
            return new_comb
        if n >= 1:
            return combinationHelper(0)
        return ""