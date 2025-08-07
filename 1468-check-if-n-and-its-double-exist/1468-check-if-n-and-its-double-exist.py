class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic = set()
        for i in range(len(arr)):
            if arr[i]*2 in dic or arr[i]/2 in dic:
                return True
            dic.add(arr[i])
        return False