class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [0 for _ in range(len(score))]
        sorted_score = sorted(score, reverse=True)
        for i, val in enumerate(sorted_score):
            ind = score.index(val)
            if i == 0:
                ans[ind] = 'Gold Medal'
            elif i == 1:
                ans[ind] = 'Silver Medal'
            elif i == 2:
                ans[ind] = 'Bronze Medal'
            else:
                ans[ind] = str(i + 1)
        return ans