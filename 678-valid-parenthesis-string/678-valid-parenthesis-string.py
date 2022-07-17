class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        def validate(s,CURR):
            bal ,wild =0,0
            for i in range(n):
                if s[i] != "*":
                    bal += 1 if s[i] == CURR else -1
                else:
                    wild += 1
                if wild + bal < 0:
                    return False
            return wild >= bal
        return validate(s,'(') and validate(s[::-1],')')