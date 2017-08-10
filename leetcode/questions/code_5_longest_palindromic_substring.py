
"""Code 5: Longest palindromic substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

Date: 2017-08-10 14:44:00
"""


class LongestPalindromicSubstringSolution(object):

    @staticmethod
    def is_palindromic_str(text):
        for i in range(0, int(len(text) / 2)):
            print(text[i], text[len(text) - i - 1])
            if text[i] != text[len(text) - i - 1]:
                return False
        return True

    @staticmethod
    def solution(text):
        """
        Solution:
        1. odd number, 
            i-2, i-1, (i), i+1, i+2
             |    +---------+    |
             +-------------------+
        
        2. even number, text[i-1] == text[i]
            i-3, i-2, (i-1, i), i+1, i+2
             |    +--------------+    |
             +------------------------+
        :param text: 
        :return: 
        """
        if len(text) <= 1:
            return text
        longest_str = text[0]
        text_length = len(text)

        def get_palindromic(f_max_r, f_up_corsur, f_down_corsur):
            exec_palindromic = ''
            for j in range(1, f_max_r + 1):
                if text[f_up_corsur - j] != text[f_down_corsur + j]:
                    exec_palindromic = text[f_up_corsur - j + 1: f_down_corsur + j]
                    break
                if f_up_corsur - j == 0 or f_down_corsur + j == text_length - 1:
                    exec_palindromic = text[f_up_corsur - j: f_down_corsur + j + 1]
                    break
            return exec_palindromic

        for i in range(1, text_length):
            current_palindromic = ''
            down_corsur = i
            if text[i] == text[i - 1]:
                max_r = i - 1 if i - 1 < text_length - i else text_length - i - 1
                up_corsur = i - 1
                current_palindromic = get_palindromic(max_r, up_corsur, down_corsur)
                current_palindromic = current_palindromic if len(current_palindromic) > 1 \
                    else text[up_corsur: down_corsur + 1]
            up_corsur = i
            max_r = i if i < text_length - i else text_length - i - 1
            current_palindromic_tmp = get_palindromic(max_r, up_corsur, down_corsur)
            current_palindromic = current_palindromic if len(current_palindromic) >= len(current_palindromic_tmp) \
                else current_palindromic_tmp

            current_palindromic = current_palindromic if len(current_palindromic) > 1 else text[up_corsur: down_corsur + 1]
            longest_str = longest_str if len(longest_str) > len(current_palindromic) else current_palindromic

        return longest_str

    @staticmethod
    def test():
        longest_str = LongestPalindromicSubstringSolution.solution('abcbc')
        print(longest_str)
        longest_str = LongestPalindromicSubstringSolution.solution('abcdbb')
        print(longest_str)
        longest_str = LongestPalindromicSubstringSolution.solution('bb')
        print(longest_str)
        longest_str = LongestPalindromicSubstringSolution.solution('cwwb')
        print(longest_str)
        longest_str = LongestPalindromicSubstringSolution.solution('caaab')
        print(longest_str)

LongestPalindromicSubstringSolution.test()
