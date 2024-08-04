"""
Question:
给定一个长度为n的数组 nums ，元素按从小到大的顺序排列且不重复。
请查找并返回元素 target 在该数组中的索引。
若数组不包含该元素，则返回 -1。

算法逻辑：
1.首先初始化left=0, right=n-1, 即数组的左右边界，代表搜索区间[0, n - 1]
2.计算中点索引 m = [(left + right) / 2]，向下取整
3.判断 nums[m] 和 target 的大小关系：
   a.若 nums[m] < target，则 target 在中值的右边，更新 left = m + 1
   b.若 nums[m] > target，则 target 在中值的左边，更新 right = m - 1
   c.若 nums[m] == target，则找到了 target，返回 m
4.重复步骤2-3，直到 left > right，即搜索区间为空，未找到 target，返回 -1
"""

# 二分查找
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
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
    idx = binary_search(nums, target)
    print(f"元素 {target} 的插入点的索引为 {idx}")



