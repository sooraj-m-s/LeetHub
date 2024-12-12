class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            for j in range(i, len(words)):
                if words[i] == words[j][::-1] and i != j:
                    ans += 1
        return ans