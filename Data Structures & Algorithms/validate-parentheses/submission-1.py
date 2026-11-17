class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'{': '}', '[': ']', '(': ')'}

        for b in s:
            if b in match:
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if match[last] != b:
                    return False
        
        return len(stack) == 0

