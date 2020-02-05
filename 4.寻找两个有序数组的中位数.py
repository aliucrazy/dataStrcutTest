#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 排序整合
        nums=list()
        if nums1 and nums2:
            if nums1[-1] < nums2[0]:
                nums += nums1
                nums += nums2
            elif nums2[-1] < nums1[0]:
                nums += nums2
                nums += nums1
            else:
                index_num2 = 0
                index_num1 = 0
                for num1_index in range(len(nums1)):
                    for num2_index in range(index_num2,len(nums2)):
                        if nums1[num1_index] < nums2[num2_index]:
                            nums.append(nums1[num1_index])
                            index_num1 +=1
                            break
                        else:
                            nums.append(nums2[num2_index])
                            index_num2 +=1
                if index_num2 != len(nums2):
                    nums +=nums2[index_num2:]
                if index_num1 !=len(nums1):
                    nums +=nums1[index_num1:]
        else:
            nums = list(nums1) if nums1 else list(nums2)
                        

            

        # 获取中位数
        if len(nums) % 2 == 0:
            # 如果能被2整除
            # 取
            return (nums[(len(nums)//2)-1] + nums[len(nums)//2])/2
        else:
            return nums[(len(nums)//2)]
        # @lc code=end

if __name__ == "__main__":
    nums1 = []
    nums2 = [2,3]
    num = Solution().findMedianSortedArrays(nums1,nums2)
    print(num)
