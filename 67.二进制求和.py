#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (51.30%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    51.1K
# Total Submissions: 99.3K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 
# 输入为非空字符串且只包含数字 1 和 0。
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#

# @lc code=start
class Solution:
    #重点在于区分出三种不同的状态，异或。
    def addBinary(self, a: str, b: str) -> str:
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            #相同为1则在末尾添加10，继续比较下一位
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            #相同为0，末尾添加0
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            #不同置1
            return self.addBinary(a[0:-1],b[0:-1])+'1'

            


# @lc code=end

