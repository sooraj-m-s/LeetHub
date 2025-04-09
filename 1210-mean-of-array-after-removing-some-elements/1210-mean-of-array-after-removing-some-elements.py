class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        l = (len(arr)*5)//100
        temp = arr[l:-l]
        return sum(temp) / len(temp)