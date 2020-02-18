#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.07%)
# Likes:    1351
# Dislikes: 0
# Total Accepted:    120.8K
# Total Submissions: 441.1K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
#
#

# @lc code=start


class Solution:
    def valid(self,s):
        if len(s) < 2:
            return True
        if s[-1] == s[0]:
            return self.valid(s[1:-1])
        if s[-1] != s[0]:
            return False

    def getchildS(self,s):
        # 获取所有字串
        childS = []
        for i in range(1,len(s)+1):
            # i代表子串长度
            for j in range(len(s)):
                # j 代表从第j位开始截取
                if len(s[j:])>=i:
                    childS.append(s[j:j+i]) 
        return childS

    def longestPalindrome(self, s: str) -> str:
        data = filter(self.valid,self.getchildS(s))
        length = 0
        longest_palindromic = ""
        for a in data:
            if len(a)>length:
                length = len(a)
                longest_palindromic = a
        return longest_palindromic
# @lc code=end


def valid(s):
    if len(s) < 2:
        return True
    if s[-1] == s[0]:
        return valid(s[1:-1])
    else:
        return False

def getchildS(s):
    # 获取所有字串
    childS = []
    for i in range(2,len(s)+1):
        # i代表子串长度
        for j in range(len(s)):
            # j 代表从第j位开始截取
            if len(s[j:])>=i:
                childS.append(s[j:j+i]) 
    return childS

if __name__ == "__main__":
    length = 0
    longest_palindromic = ""
    StrList = getchildS("babad")
    data = filter(valid,StrList)
    for a in data:
        if len(a)>length:
            length = len(a)
            longest_palindromic = a
    print(longest_palindromic)