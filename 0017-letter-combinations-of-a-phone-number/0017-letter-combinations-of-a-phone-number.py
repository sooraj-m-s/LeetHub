class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if not digits:
            return []
        
        ans = ['']
        for i in digits:
            temp = comb[i]
            new = []
            for j in ans:
                for k in temp:
                    new.append(j + k)
            ans = new
        return ans