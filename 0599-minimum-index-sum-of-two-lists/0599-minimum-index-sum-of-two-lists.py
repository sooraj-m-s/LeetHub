class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = {}
        for i, j in enumerate(list1):
            if j in list2:
                ind = list1.index(j) + list2.index(j)
                if ind in ans:
                    ans[ind].append(j)
                else:
                    ans[ind] = [j]
        temp = min(ans.keys())
        return ans[temp]