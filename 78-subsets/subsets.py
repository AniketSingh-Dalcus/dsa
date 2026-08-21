class Solution(object):
    def subsets(self, nums):
        result = []

        def backtrack(index, current):
            if index == len(nums):
                result.append(current[:])
                return

            # Take nums[index]
            current.append(nums[index])
            backtrack(index + 1, current)

            # Don't take nums[index]
            current.pop()
            backtrack(index + 1, current)

        backtrack(0, [])
        return result
