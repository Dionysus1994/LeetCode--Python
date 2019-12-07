#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (53.22%)
# Likes:    344
# Dislikes: 0
# Total Accepted:    60.4K
# Total Submissions: 113.1K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
# 
# 注意：整数顺序将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 
#

# @lc code=start
class Solution:
    #解题思路关键在于取出连续相同的单个字符

    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit#，
                    #re.findall 正则函数，r为正则表达
                    # .为除\n以外的任意单字符
                    # \2*，2为找寻字符串中所有的2，*表示2可以不出现或者出现一次或多次
                    # 以上，每次找到2时，2前面的部分划分入group，之后的部分为dight

                    for group, digit in re.findall(r'((.)\2*)', s))
        return s
# @lc code=end

