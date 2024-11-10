class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for i in sentences:
            temp = i.split()
            if len(temp) > ans:
                ans = len(temp)
        return ans