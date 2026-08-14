class Solution(object):
    def containsDuplicate(self, nums):
        hash_list=set()
        for num in nums:
            if num in hash_list:
                return True
            hash_list.add(num)
        return False



        