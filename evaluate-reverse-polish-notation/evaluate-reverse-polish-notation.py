class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return tokens[0]
        def operation(left,right,token):
            left = int(left)
            right = int(right)
            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)
        ops = ['/','+','-','*']
        stack = []
        res = None
        for token in tokens:
            if token in ops:
                if res is None:
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(operation(left,right,token))
            else:
                stack.append(int(token))
        return stack.pop()