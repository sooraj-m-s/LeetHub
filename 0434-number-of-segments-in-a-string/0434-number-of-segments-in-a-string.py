class Solution:
    def countSegments(self, s: str) -> int:
        count, inside = 0, False
        for i in s:
            if i != ' ' and not inside:
                count += 1
                inside = True
            elif i == ' ':
                inside = False
        return count