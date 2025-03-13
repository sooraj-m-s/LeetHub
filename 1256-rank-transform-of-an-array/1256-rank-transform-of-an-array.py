class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        index_dic = {val: key + 1 for key, val in enumerate(sorted_unique)}
        return [index_dic[i] for i in arr]