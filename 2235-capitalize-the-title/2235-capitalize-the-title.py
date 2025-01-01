class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = title.split(' ')
        for i, j in enumerate(ans):
            if len(j) > 2:
                ans[i] = j.title()
            else:
                ans[i] = j.lower()
        return ' '.join(ans)