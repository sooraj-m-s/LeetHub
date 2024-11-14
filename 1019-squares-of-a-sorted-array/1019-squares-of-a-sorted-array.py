class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [i*i for i in nums]
        # for i in range(len(ans)):
        #     for j in range(len(ans)):
        #         if ans[i] < ans[j]:
        #             temp = ans[i]
        #             ans[i] = ans[j]
        #             ans[j] = temp
        return sorted(ans)