"""
- Trapping rain water -
Given an array of integers representing heights of objects, find the maximum
'volume' of rain that can be help within these objects.

Start by assuming that the right endpoint has a maximum of INF.
Sweep from left to right: keep track of the maximum (m). If an object height (h) is less
than the maximum, we can fill (h-m) units of water.
Next assume that the left endpoint has a maximum of INF and sweep from right to left.
To remove the initial assumption of a left/right INF boundary, we construct an array
where each element in the new array is the minimum of the left and right arrays elements.
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = [0] * len(height)
        right = [0] * len(height)
        max_height = 0
        
        for i in range(0, len(height)):
            max_height = max(max_height, height[i])
            if max_height > height[i]:
                left[i] = max_height - height[i]
        max_height = 0
        
        for i in range(len(height) - 1, -1, -1):
            max_height = max(height[i], max_height)
            if max_height > height[i]:
                right[i] = max_height - height[i]
        max_sum = 0
        
        for x in range(len(height)):
            max_sum += min(left[x],  right[x])
        return max_sum
