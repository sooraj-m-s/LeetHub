class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_one = 0
        max_row = 0
        for i, j in enumerate(mat):
            cnt_one = j.count(1)
            if cnt_one > max_one:
                max_one = cnt_one
                max_row = i
        return [max_row, max_one]