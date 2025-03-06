class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        temp, operations = set(), 0
        for i in reversed(nums):
            operations += 1
            if i <= k:
                temp.add(i)
            if len(temp) == k:
                return operations
        return operations