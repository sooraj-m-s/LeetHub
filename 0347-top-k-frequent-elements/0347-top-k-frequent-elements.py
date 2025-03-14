class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency, ans = {}, []
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        sorted_ans = dict(sorted(frequency.items(), key=lambda x : x[1], reverse=True))
        for i, j in sorted_ans.items():
            ans.append(i)
            if len(ans) >= k:
                break
        return ans