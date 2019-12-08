#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (60.60%)
# Likes:    379
# Dislikes: 0
# Total Accepted:    89.8K
# Total Submissions: 147.9K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #摩尔算法，每次遇到不同的匹配就删除，最后剩下的必然是出现最多的。
        stack = 0
        top = 0
        for i in range(len(nums)):
            #初次赋值
            #以及当每次栈为空，即top为0
            #类似于栈，每次取栈顶元素比较，若不相同，则出栈,若相同，则入栈。
            #此处不断相同，则不断重复赋值，直到结束
            if top == 0:
                stack = nums[i]
                top = 1
            else:
                if nums[i] == stack:
                    top += 1
                else:
                    top -= 1
        return stack
                
# @lc code=end

