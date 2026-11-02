class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_ctr = {};
        for cs in s:
            if cs not in char_ctr:
                char_ctr[cs] = 1;
            else:
                char_ctr[cs] += 1;
        
        for ct in t:
            if ct not in char_ctr:
                char_ctr[ct] = -1;
            else:
                char_ctr[ct] -= 1;
        
        for k, v in char_ctr.items():
            if v != 0:
                return False;

        return True;
        