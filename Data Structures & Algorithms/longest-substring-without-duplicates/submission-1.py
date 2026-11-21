class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        chars = set()
        mx_len = 0

        i = 0
        j = 0

        while j < len(s):
            # print("checking: " + s[i:j + 1])
            if s[j] not in chars:
                chars.add(s[j])
            else:
                mx_len = max(mx_len, j - i)

                while s[i] != s[j]:
                    # print("running: " + s[i:j + 1])
                    chars.remove(s[i])
                    i += 1
                
                i += 1
            
            j += 1
        
        mx_len = max(mx_len, j - i)

        return mx_len


