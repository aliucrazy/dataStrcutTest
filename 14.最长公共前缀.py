#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.78%)
# Likes:    810
# Dislikes: 0
# Total Accepted:    163.8K
# Total Submissions: 460.4K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        initial_data = strs[0]
        longest_index = len(strs[0])
        for data in strs[1:]:
            print('当前元素为: '+data)
            # 如果长度不一致呢
            for data_index in range(len(data)):
                if data[data_index] != initial_data[data_index]:
                    print(f'当前元素的第{str(data_index)}不再一致')
                    # 此时出现不一致情况 应当替换当前最长公共前缀索引
                    longest_index = min(longest_index, data_index - 1)
                    break
        return initial_data[:longest_index]


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    data = Solution().longestCommonPrefix(strs)
    print(data)
