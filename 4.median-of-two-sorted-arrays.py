#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def median(self, n, nums):
        if n == 1:
            return float(nums[0])
        elif nums == 2:
            return (nums[0] + nums[1])/2
        elif n % 2 == 0:
            return (nums[n//2] + nums[n//2-1])/2
        elif n % 2 == 1:
            return float(nums[(n+1)//2-1])
    def MaxMin(self, num1, num2):
        if num1>num2:
            return num1, num2 
        else:
            return num2, num1
    def check(self, arr, item):
        i = -1
        while(item<arr[i]):
            if abs(i) == len(arr):
                return -1
            i -= 1
        return i

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n + m == 0:
            return float(0)
        elif n == 0:
            return self.median(m, nums2)
        elif m == 0:
            return self.median(n, nums1)
        else:
            sorted_arr = []
            i = 0
            j = 0
            end_index = (n + m)//2 if (n+m)%2 == 0 else (n+m+1)//2 - 1
            while(len(sorted_arr)<n+m):
                if i<n and j<m:
                    high, low = self.MaxMin(nums1[i], nums2[j])
                    if len(sorted_arr)>0:
                        if low >= sorted_arr[-1]:
                            sorted_arr.append(low)
                            sorted_arr.append(high)
                        else:
                            if high >= sorted_arr[-1]:
                                index = self.check(sorted_arr, low)
                                sorted_arr.insert(index+1, low)
                                sorted_arr.append(high)
                            else:
                                index = self.check(sorted_arr, low)
                                sorted_arr.insert(index+1, low)
                                index = self.check(sorted_arr, high)
                                sorted_arr.insert(index+1, low)
                    else:
                        sorted_arr.append(low)
                        sorted_arr.append(high)
                elif i<n:
                    if len(sorted_arr)>0:
                        if nums1[i] >= sorted_arr[-1]:
                            sorted_arr.extend(nums1[i:])
                        else:
                            index = self.check(sorted_arr, nums1[i])
                            sorted_arr.insert(index+1, nums1[i])
                elif j<m:
                    if len(sorted_arr)>0:
                        if nums2[j] >= sorted_arr[-1]:
                            sorted_arr.extend(nums2[j:])
                        else:
                            index = self.check(sorted_arr, nums2[j])
                            sorted_arr.insert(index+1, nums2[j])
                else: 
                    break
                i+=1
                j+=1
            return float(sorted_arr[end_index]) if (n+m)%2 == 1 else (sorted_arr[end_index] + sorted_arr[end_index-1])/2




        
# @lc code=end

