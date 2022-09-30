#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def calculateArea(self, h1, i, h2, j):
        height = h1 if h1< h2 else h2
        length = j - i if j>i else i-j
        return height*length

    def maxArea(self, height: List[int]) -> int:
        max1 = max(height)
        if max1 == height[-1]:
            height = height[::-1]
        max_area = 0
        prev = 0
        i = 0
        j = 1
        while(i<len(height)-1):
            if height[i] > prev:
                while(j<len(height)):
                    area = self.calculateArea(height[i], i, height[j], j)
                    if area > max_area:
                        max_area = area
                    j+=1
                prev = height[i]
            i += 1
            j = i + 1
        return max_area
                

        
# @lc code=end

