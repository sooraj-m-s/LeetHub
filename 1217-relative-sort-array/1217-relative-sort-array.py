class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        cnt, result = Counter(arr1), []
        for i in arr2:
            result.extend([i] * cnt.pop(i))
        result.extend(sorted(cnt.elements()))
        return result