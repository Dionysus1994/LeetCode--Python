#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (58.28%)
# Likes:    718
# Dislikes: 0
# Total Accepted:    142K
# Total Submissions: 243.3K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:#l1或者l2是否到尾部，或者是否为空。递归到一方为空
            return l2#最后一次循环时，将剩下的加入链表尾部（有序链表，故后续无需继续排列比较
        elif l2 == None:
            return l1
        elif l1.val < l2.val:#l1的值如果小于l2的
            l1.next = self.mergeTwoLists(l1.next,l2)#继续判断l1.next与l2，直到l2大于l1
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)#同理，直到l1大于l2
            return l2
# @lc code=end

