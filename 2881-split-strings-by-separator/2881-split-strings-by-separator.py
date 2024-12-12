class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for i in words:
            temp = i.split(separator)
            for j in temp:
                if j != '':
                    ans.append(j)
        return ans