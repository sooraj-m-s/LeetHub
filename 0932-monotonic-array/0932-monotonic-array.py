class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # asc = nums.copy()
        # for i in range(len(asc)):
        #     for j in range(len(asc)):
        #         if asc[i] < asc[j] and i != j:
        #             temp = asc[i]
        #             asc[i] = asc[j]
        #             asc[j] = temp
        # desc = asc[::-1]
        # if asc == nums or desc == nums:
        #     return True
        # return False
        if sorted(nums) == nums or sorted(nums, reverse=True) == nums:
            return True
        return False