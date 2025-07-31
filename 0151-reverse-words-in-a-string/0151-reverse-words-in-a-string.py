class Solution:
    def reverseWords(self, s: str) -> str:
        # s_list = s.strip().split()
        # ans = ''
        # for i in range(len(s_list)-1, -1, -1):
        #     ans += s_list[i]
        #     if i > 0:
        #         ans += ' '
        # return ans
        
        return ' '.join(s.strip().split()[::-1])