class Solution:
    def sortVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = 'AEIOUaeiou'
        sorted_vowels = sorted(i for i in s_list if i in vowels)
        vowel_index = 0
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = sorted_vowels[vowel_index]
                vowel_index += 1
        return ''.join(s_list)