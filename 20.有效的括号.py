#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.05%)
# Likes:    1187
# Dislikes: 0
# Total Accepted:    155.3K
# Total Submissions: 387.5K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
# @lc code=start
class Solution:
    def isValid(self, s):
        #初始化数据
        stack, match = [], {')': '(', ']': '[', '}': '{'}
        for ch in s:#遍历输入数据
            if ch in match:#成对匹配括号，在定义时反向定义，不匹配的括号
                if not (stack and stack.pop() == match[ch]):#如果栈不为空，取出栈顶元素判断是否为不匹配括号
                    return False
            else:
                stack.append(ch)#向栈底插入值
        return not stack#
# @lc code=end

