"""
Binary Search in a rotated array.
Given an array that may be rotated, find the index of the target value.

Binary search can still be applied in this situation but we need to be extra careful
of which interval to narrow down to. We will consider an interval in which the
left endpoint is lesser than the right endpoint. This means that this interval of the
array is sorted. If our target is within this interval, then we can narrow down to
this interval.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        if len(nums) < 4:
            return nums.index(target)
        while left != right and left + 1 != right:
            middle = (right + left)//2
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[middle] == target:
                return middle
            if nums[left] < nums[middle]:
                if nums[left] < target < nums[middle]:
                    right = middle
                else:
                    left = middle
            elif nums[middle] < nums[right]:
                if nums[middle] < target < nums[right]:
                    left = middle
                else:
                    right = middle
        if nums[left] == target:
            return left
        return -1
        
