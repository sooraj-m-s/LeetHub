class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        temp = [i for j in grid for i in j]
        repeat = 0
        missing = 0
        for i in range(len(temp)):
            for j in range(len(temp)):
                if temp[i] == temp[j] and i != j:
                    repeat = temp[i]
        for i in range(1, len(temp)+1):
            if i in temp:
                temp.remove(i)
            else:
                return [repeat, i]