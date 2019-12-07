#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        j = 0
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        while x > j:
            j = j * 10 + x % 10
            x = int(x/10)
            
   
        return x == j or x == int(j/10)
        
# @lc code=end
class test:
    if __name__ == "__main__": 
        x = 121
        y = Solution.isPalindrome(0,x)
        
        



