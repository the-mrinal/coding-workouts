class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
        "IV": 4,
        "IX": 9,
        "XL": 40, 
        "XC": 90,
        "CD": 400,
        "CM": 900  
        }
        
        number = 0
        n = len(s)
        i = 0
        while i < n:
            if i < len(s) -1 and s[i:i+2] in hashMap:
                number += hashMap[s[i:i+2]]
                i = i + 2
            else:
                number = number + hashMap[s[i]]
                i += 1
                
        return number