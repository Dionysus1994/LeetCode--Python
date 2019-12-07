#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (47.22%)
# Likes:    731
# Dislikes: 0
# Total Accepted:    107.7K
# Total Submissions: 227.6K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        #f(n) = f(n - 1) + f(n - 2)
        #f(1) = 1 f(2) = 2 f(3) = 3 f(4) = 5
        # 每次只能跳一或两阶，所以 
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(2,n):
            third = first + second
            first = second
            second = third
        return second

 # @lc code=end

