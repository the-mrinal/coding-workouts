'''
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
10 -1 

'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+','-','*','/']
        
        def operate(left,right,op):
            if(op == '+'):
                return left + right
            if(op == '-'):
                return left - right
            if(op == '*'):
                return left * right
            if(op == '/'):
                return int(left / right)
        
        for char in tokens:
            if char in operations:
                right = stack.pop()
                left = stack.pop()
                curr = operate(left,right,char)
                stack.append(curr)
            else:
                stack.append(int(char))
        
        return stack.pop()