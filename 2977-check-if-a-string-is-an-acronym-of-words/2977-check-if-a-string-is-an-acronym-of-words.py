class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        temp = ''.join([i[0] for i in words])
        return temp == s