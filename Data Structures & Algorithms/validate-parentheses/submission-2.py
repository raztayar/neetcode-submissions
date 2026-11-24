class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for ch in s:
            if ch in close_to_open:
                if not stack:
                    return False
                
                last = stack.pop()
                if last != close_to_open[ch]:
                    return False
            else:
                stack.append(ch)
        
        if stack:
            return False
        
        return True