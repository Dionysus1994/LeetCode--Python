#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#
# https://leetcode-cn.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (65.52%)
# Likes:    93
# Dislikes: 0
# Total Accepted:    26K
# Total Submissions: 39.5K
# Testcase Example:  '"A"'
#
# 给定一个Excel表格中的列名称，返回其相应的列序号。
# 
# 例如，
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: "A"
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: "AB"
# 输出: 28
# 
# 
# 示例 3:
# 
# 输入: "ZY"
# 输出: 701
# 
# 致谢：
# 特别感谢 @ts 添加此问题并创建所有测试用例。
# 
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        #26进制与ascii码
        power = len(s)
        excel_listnum = 0
        for i in range(power):
            #记录每一位
            temp = (ord(s[i])-64) *pow(26,power - i - 1) 
            excel_listnum += temp
        return excel_listnum
# @lc code=end

