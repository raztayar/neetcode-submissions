class Solution:
    D = {}

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s
        
        self.D[res] = strs

        return res

    def decode(self, s: str) -> List[str]:
        return self.D[s]