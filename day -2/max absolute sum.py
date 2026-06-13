class Solution:
    def maxAbsoluteSum(self, nums):

        curr_max = 0
        curr_min = 0

        max_sum = 0
        min_sum = 0

        for num in nums:

            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, -min_sum)
