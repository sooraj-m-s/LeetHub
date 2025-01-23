class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        left, vowels_cnt = 0, 0
        vowels = 'AEIOUaeiou'
        vowels_list = [i for i in s_list if i in vowels]
        vowels_list.reverse()
        while left < len(s):
            if s_list[left] in vowels:
                s_list[left] = vowels_list[vowels_cnt]
                vowels_cnt += 1
            left += 1
        return ''.join(s_list)