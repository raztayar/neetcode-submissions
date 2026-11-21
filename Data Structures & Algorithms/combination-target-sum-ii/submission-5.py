class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        C = Counter(candidates)
        cand_list = list(C.keys())
        print (cand_list)
        res = []

        temp_lst = []
        temp_sum = 0
        
        def dfs(i):
            nonlocal temp_sum

            if i == len(cand_list):
                return
            
            for j in range(i, len(cand_list)):
                # print(j)

                temp_lst.append(cand_list[j])
                temp_sum += cand_list[j]
                C[cand_list[j]] -= 1
                # print("trying: ", temp_lst)

                if temp_sum == target:
                    # print("success")
                    res.append(temp_lst.copy())
                
                elif temp_sum < target:
                    # print("not enough")
                    if C[cand_list[j]] == 0:
                        dfs(j + 1)
                    else:
                        dfs(j)

                # else:
                    # print("too much")
                
                C[cand_list[j]] += 1
                temp_sum -= cand_list[j]
                temp_lst.pop()
        
        dfs(0)
        return res
            
        
                    

            

            

            


