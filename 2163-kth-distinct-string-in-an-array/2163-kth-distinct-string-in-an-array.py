from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        temp=""
        distinct=[]
        for i in arr:
            if arr.count(i)==1:
                distinct.append(i)
        if k<=len(distinct):
            return distinct[k-1]
        return ""

arr = ["d","b","c","b","c","a"]
k=2
s=Solution()
result=s.kthDistinct(arr,k)
print(result)