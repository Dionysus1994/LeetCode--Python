#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (65.52%)
# Likes:    667
# Dislikes: 0
# Total Accepted:    127.9K
# Total Submissions: 194.3K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #迭代的方法关键在于，prev，即每一个next指向前一个结点，最前的结点prev指向NULL
        #此处为递归，后进先出，所以非常适合反转
        if head == None or head.next == None:#直到链表尾，返回head
            return head 
        p = self.reverseList(head.next)#不断递归，直到链表尾
        head.next.next = head
        head.next = None
        return p
# @lc code=end

