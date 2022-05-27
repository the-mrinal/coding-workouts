class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                local = ""
                while stack:
                    curr = stack.pop()
                    if curr == "[":
                        break
                    local = curr + local
                
                num = 0
                count = 1
                while stack:
                    if ord(stack[-1]) >= 48 and ord(stack[-1]) <= 57:
                        currNum = int(stack.pop())
                        currNum = currNum * count
                        num = num + currNum
                        count = count * 10
                    else:
                        break
                
                local = num * local
                
                for i in local:
                    stack.append(i)
        
        return ''.join(stack)
                