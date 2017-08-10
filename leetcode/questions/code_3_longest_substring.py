
"""
Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
Given a string, find the length of the longest substring without repeating characters.

Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, 
        "pwke" is a subsequence and not a substring.

Date: 2017-08-10 10:55:00
"""


class LengthOfLongestSubstringSolution(object):

    @staticmethod
    def solution(text):
        longest_str = ''
        longest_len = 0
        different_str = ''
        for s in text:
            if s in different_str:
                if s != different_str:
                    new_str = different_str[different_str.index(s) + 1: len(different_str)]
                    different_str = new_str + s
            else:
                different_str += s
            longest_len = longest_len if longest_len >= len(different_str) else len(different_str)
            longest_str = longest_str if len(longest_str) >= len(different_str) else different_str
        return longest_len

    @staticmethod
    def test():
        LengthOfLongestSubstringSolution.solution('abcabcbb')
        LengthOfLongestSubstringSolution.solution('bbbbb')
        LengthOfLongestSubstringSolution.solution('pwwkew')


LengthOfLongestSubstringSolution.test()
