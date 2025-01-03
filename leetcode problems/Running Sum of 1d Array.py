# https://leetcode.com/problems/running-sum-of-1d-array/description/

# Description:
# Given an array nums. We define a running sum of an array as
# # runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

nums = [1, 2, 3, 4, 5]

def sum_num(nums):
    sum_nums = []
    for index in range(0, len(nums)):
        #create sub arrays of list, beginning at 0 and ending at current for loop value
        sub_array = nums[0:index+1:1]
        sum_nums.append(sum(sub_array))
    print(sum_nums)
sum_num(nums)