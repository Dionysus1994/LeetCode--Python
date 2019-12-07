#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (37.21%)
# Likes:    259
# Dislikes: 0
# Total Accepted:    75.9K
# Total Submissions: 203.9K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 

# @lc code=start
class Solution:
    def mySqrt(self, x):
        left, right = 0, x
        while left <= right:
            #中值赋值，一个数的平发根不会大于该数的中值
            mid = left + (right-left)//2 
            #因为返回类型为整数，无小数点，所以x只需要小于 mid + 1的平方
            #此处1为精度
            if mid * mid <= x < (mid+1)*(mid+1):

                return mid
            elif x < mid * mid:
                right = mid#如果mid过大，右边边界左移
            else:
                left = mid + 1#反之mid过小，左边界右移，1为精度
# @lc code=end

