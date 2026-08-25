class Solution(object):
    def runningSum(self, nums):
        arr = [0] * len(nums)
        arr[0] = nums[0]
        for i in range(1, len(nums)):
            j = i - 1
            arr[i] = arr[j] + nums[i]
        return arr

