class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = [i for i in nums if i % 2 == 1]
        even = [i for i in nums if i % 2 == 0]
        ans = []
        for i in range(len(odd)):
            ans += [even[i]]
            ans += [odd[i]]
        return ans