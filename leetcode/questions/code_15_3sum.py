
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class ThreeSum(object):

    @staticmethod
    def solution_2sum(arr, start, end, target, target_arr):
        left = start
        right = end
        while left < right:
            if arr[left] + arr[right] + target == 0:
                target_arr.append([target, arr[left], arr[right]])
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while right > left and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif arr[left] + arr[right] + target > 0:
                right -= 1
            elif arr[left] + arr[right] + target < 0:
                left += 1
        return target_arr

    @staticmethod
    def solution(arr):
        arr.sort()
        result_list = list()
        arr_len = len(arr)
        for i in range(0, arr_len):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            for j in range(i + 1, arr_len):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                for k in range(j + 1, arr_len):
                    if k > j + 1 and arr[k] == arr[k - 1]:
                        continue
                    if arr[i] + arr[j] + arr[k] == 0:
                        new_list = list()
                        new_list.append(arr[i])
                        new_list.append(arr[j])
                        new_list.append(arr[k])
                        result_list.append(new_list)
        return result_list

    @staticmethod
    def solution2(arr=list()):
        arr.sort()
        target_arr = list()
        print(arr)
        for i in range(0, len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            ThreeSum.solution_2sum(arr, i + 1, len(arr) - 1, arr[i], target_arr)
        return target_arr

    @staticmethod
    def test():
        result = ThreeSum.solution2([-13,10,11,-3,8,11,-4,8,12,-13,5,-6,-4,-2,12,11,7,-7,-3,10,12,13,-3,-2,6,-1,14,7,-13,8,14,-10,-4,10,-6,11,-2,-3,4,-13,0,-14,-3,3,-9,-6,-9,13,-6,3,1,-9,-6,13,-4,-15,-11,-12,7,-9,3,-2,-12,6,-15,-10,2,-2,-6,13,1,9,14,5,-11,-10,14,-5,11,-6,6,-3,-8,-15,-13,-4,7,13,-1,-9,11,-13,-4,-15,9,-4,12,-4,1,-9,-5,9,8,-14,-1,4,14])
        print(result)
        result = ThreeSum.solution2([-1,-1, 0, 1, 2, -1, -4])
        print(result)
        result = ThreeSum.solution2([0, 0, 0, 0, 0, 0])
        print(result)
        result = ThreeSum.solution2([1,-1,-1,0])
        print(result)
        result = ThreeSum.solution2([-1, 0, 1, 2, -1, -4])
        print(result)
        result = ThreeSum.solution2([3,0,-2,-1,1,2])
        print(result)
        result = ThreeSum.solution2([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
        print(result)
        result = ThreeSum.solution2([-1,0,1,2,-1,-4])
        print(result)


ThreeSum.test()
