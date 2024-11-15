class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        # if len(words) != len(s):
        #     return False
        # for i,j in enumerate(words):
        #     if j[0] != s[i]:
        #         return False
        # return True
        temp = ''.join([i[0] for i in words])
        return temp == s