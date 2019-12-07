#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (48.05%)
# Likes:    1390
# Dislikes: 0
# Total Accepted:    128.2K
# Total Submissions: 265.8K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        val = nums[0]
        for n in nums:
            #遍历数组不断累加，留下累加过程中的最大值
            #如果为负数，则只需要比较单个元素大小，取最大值
            if sum > 0:
                sum +=n 
            else:
                sum = n
            val = max(sum,val)
        return val
            
            
# @lc code=end

