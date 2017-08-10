
"""
Reference https://leetcode.com/problems/two-sum/#/description
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    
Date: 2017-08-10 10:55:00
"""


class TwoSumSolution(object):

    @staticmethod
    def solution(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        return [0, 0]

    @staticmethod
    def test():
        result = TwoSumSolution.solution([2, 7, 11, 15], 18)
        print(result)


TwoSumSolution.test()
