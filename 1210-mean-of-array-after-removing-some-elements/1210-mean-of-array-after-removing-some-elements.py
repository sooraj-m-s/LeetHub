class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        temp_li = arr[round(len(arr)*5/100):-round(len(arr)*5/100)]
        return sum(temp_li)/len(temp_li)