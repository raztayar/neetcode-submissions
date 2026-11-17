class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        def str_to_tup(s: str) -> tuple:
            s_list = [0 for _ in range(0, 26)]
            for c in s:
                s_list[ord(c) - ord('a')] += 1

            return tuple(s_list)
        
        grouper = {}

        for s in strs:
            curr_tup = str_to_tup(s)
            if grouper.get(curr_tup):
                grouper[curr_tup].append(s)
            else:
                grouper[curr_tup] = [s]
        
        for _, ls in grouper.items():
            res.append(ls)
        
        return res
    

