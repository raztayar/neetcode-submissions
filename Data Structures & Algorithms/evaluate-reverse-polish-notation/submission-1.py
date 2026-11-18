import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = b = 0
        stack = []
        op = {"+": lambda a,b: a+b , 
            "*" : lambda a,b: a*b, 
            "-" : lambda a,b: a-b, 
            "/" : lambda a,b: a/b}

        for t in tokens:
            if t in op:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(op[t](b,a)))
            else:
                stack.append(int(t))
        
        return stack.pop()
            
