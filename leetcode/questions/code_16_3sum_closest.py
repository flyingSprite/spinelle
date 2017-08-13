
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
import math
import sys


class ThreeSumClosest(object):

    @staticmethod
    def solution_2sum(arr, start, end, prev, target):
        left = start
        right = end
        sum_value = sys.maxsize
        fabs_value = sys.maxsize
        while left < right:
            current_fabs = math.fabs(arr[left] + arr[right] + prev - target)
            if current_fabs < fabs_value:
                sum_value = arr[left] + arr[right] + prev
                fabs_value = current_fabs
            if arr[left] + arr[right] + prev == target:
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while right > left and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif arr[left] + arr[right] + prev > target:
                right -= 1
            elif arr[left] + arr[right] + prev < target:
                left += 1
        return sum_value

    @staticmethod
    def solution(arr=list(), target=0):
        arr.sort()
        closest_value = sys.maxsize
        for i in range(0, len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            sum_value = ThreeSumClosest.solution_2sum(arr, i + 1, len(arr) - 1, arr[i], target)
            closest_value = closest_value if math.fabs(target - closest_value) < math.fabs(target - sum_value) \
                else sum_value
        return closest_value

    @staticmethod
    def test():
        result = ThreeSumClosest.solution([-1, 2, 1, -4], 2)
        print(result)
        result = ThreeSumClosest.solution([0, 0, 0], 1)
        print(result)
        result = ThreeSumClosest.solution([0, 1, 2], 0)
        print(result)
        result = ThreeSumClosest.solution([0,2,1,-3], 1)
        print(result)
        result = ThreeSumClosest.solution([1,2,5,10,11], 12)
        print(result)


ThreeSumClosest.test()
