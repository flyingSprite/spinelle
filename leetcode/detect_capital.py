
"""
Reference: https://leetcode.com/contest/leetcode-weekly-contest-20/problems/detect-capital/
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
    Input: "USA"
    Output: True
    
Example 2:
    Input: "FlaG"
    Output: False
"""


class Solution(object):

    @staticmethod
    def detect_capital_use(word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False
        start_with_uppercase = word[0] >= 'A' and (word[0] <= 'Z')
        upper_count = 0
        for i in range(len(word)):
            if word[i] >= 'A' and (word[i] <= 'Z'):
                upper_count += 1
            if upper_count != 0 and upper_count != i + 1 and not (upper_count == 1 and start_with_uppercase):
                return False

        if upper_count == 0:
            return True

        if upper_count == len(word):
            return True

        if upper_count == 1 and start_with_uppercase:
            return True

        return False
