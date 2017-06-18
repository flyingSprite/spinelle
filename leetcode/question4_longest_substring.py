
"""
Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
Given a string, find the length of the longest substring without repeating characters.

Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # longest_substring_tmp = ''
        # longest_substring = ''
        # for i in range(len(s)):
        #     if s[i] not in longest_substring:
        #         longest_substring += longest_substring
        #     else:
        #         ''
        # return s.index('a')
        longest_substring_index_tmp = [0, 0]
        longest_substring_index = [0, 0]

solution = Solution()
print(solution.lengthOfLongestSubstring('sssafff'))
