#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (48.20%)
# Likes:    229
# Dislikes: 0
# Total Accepted:    58.9K
# Total Submissions: 121.8K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head #头指针传递
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # 删除重复结点
            cur = cur.next     # 跳过重复结点后的第一个结点
        return head #返回的是头指针，cur最终指向NULL
# @lc code=end

