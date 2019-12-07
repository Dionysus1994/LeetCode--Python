#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (31.51%)
# Likes:    149
# Dislikes: 0
# Total Accepted:    54.6K
# Total Submissions: 172.7K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i>=0 and s[i] == " ":#找寻末尾第一个空格
            i-=1
        if i < 0:#如果字符串只有空格
            return 0
        j = i
        while j>=0 and s[j] !=" ":#末尾第一个空格到下一个空格的距离，若没有下一个空格，j为0
            j-=1
        

        return i - j
# @lc code=end

