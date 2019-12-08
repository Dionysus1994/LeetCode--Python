#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (35.47%)
# Likes:    150
# Dislikes: 0
# Total Accepted:    16K
# Total Submissions: 44.7K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 
# 例如，
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "A"
# 
# 
# 示例 2:
# 
# 输入: 28
# 输出: "AB"
# 
# 
# 示例 3:
# 
# 输入: 701
# 输出: "ZY"
# 
# 
#

# @lc code=start

class Solution:
    def convertToTitle(self, n: int) -> str:
        #26进制与ascii码
        excel_name = ''
        while n:
            temp = (n-1) % 26
            excel_name = chr(temp + 65) + excel_name
            n -= temp
            n //= 26
        return excel_name
# @lc code=end

