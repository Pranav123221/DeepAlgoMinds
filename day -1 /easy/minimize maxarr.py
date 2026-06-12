class Solution:
    def minimizeArrayValue(self, nums):
        prefix_sum = 0
        answer = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            answer = max(
                answer,
                (prefix_sum + i) // (i + 1)
            )

        return answer