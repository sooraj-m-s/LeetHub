class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i,j in enumerate(nums):
            temp = target - j
            if temp in result:
                return [result[temp], i]
            else:
                result[j] = i
        return []