class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        while i < j:
            while i < len(s) - 1 and not s[i].isalnum():
                i += 1
            while j > 0 and not s[j].isalnum():
                j -= 1
            
            if j < i: return True

            print(f"i = {s[i].capitalize()}|| j = {s[j].capitalize()}")
            
            if s[i].capitalize() != s[j].capitalize():
                return False
            
            i += 1
            j -= 1


        return True
