class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            word = ''.join(sorted(i))
            if word in ans:
                ans[word].append(i)
            else:
                ans[word] = [i]
        return list(ans.values())