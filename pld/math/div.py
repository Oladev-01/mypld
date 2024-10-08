#!/usr/bin/env python3
from typing import List
"""finding the smallest contiguous subarray that
can be taken from an array to give a remain by
which adding it sum will be divisible by p"""

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if p == 0 or sum(nums) < p:
            return -1
        total = sum(nums)
        # they parsed an empty nums
        if total == 0 or total % p == 0:
            print('i was here')
            return 0
        sub = []
        tar = total % p
        # [
        # --------- implementing the loop -------
        try:
            for i in range(len(nums) - 1):
                if nums[i] == tar or nums[i + 1] == tar:
                    return 1
                elif nums[i] + nums[i+1] > tar:
                    continue
                elif nums[i] + nums[i+1] == tar:
                    if not sub:
                        sub.extend([nums[i], nums[i+1]])
                    else:
                        return 2
                elif nums[i] + nums[i+1] < tar:
                    get_sum = nums[i] + nums[i+1] + nums[i+2]
                    if get_sum == tar:
                        return 3
                    else:
                        continue
            return len(sub)       
        except IndexError:
            return -1
        return -1

sol = Solution()
print(sol.minSubarray([4, 4, 7], 7))

