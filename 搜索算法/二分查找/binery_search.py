"""
给定一个长度为n的数组 nums ，元素按从小到大的顺序排列且不重复。
请查找并返回元素 target 在该数组中的索引。若数组不包含该元素，则返回 -1。
"""

# 二分查找
def binery_search(nums, target):
    left, right = 0, len(nums) - 1
    # 循环，当搜索区间为空时跳出（当 i > j 时为空）
    while left <= right:  
        m = (left + right) // 2
        if(nums[m] < target):  # target 在中值的右边
            left = m + 1
        elif nums[m] > target: # target 在中值的左边
            right = m - 1
        else:  # 找到target
            return m
    return -1  # 若数组不包含该元素，则返回 -1




if __name__ == "__main__":
    nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]
    target = 6
    idx = binery_search(nums, target)
    print(idx)















