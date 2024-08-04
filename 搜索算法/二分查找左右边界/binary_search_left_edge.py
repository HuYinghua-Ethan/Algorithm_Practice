"""
Question:
给定一个长度为 n 的有序数组 nums ，其中可能包含重复元素。请返回数组中最左一个元素 target 的索引。若数组中不包含该元素，则返回-1。

回忆二分查找插入点的方法，搜索完成后 left 指向最左一个 target ，因此查找插入点本质上是在查找最左一个 target 的索引。
考虑通过查找插入点的函数实现查找左边界。请注意，数组中可能不包含 target ，这种情况可能导致以下两种结果。
1.插入点的索引 left 越界。
2.元素 nums[left] 与 target 不相等。
当遇到以上两种情况时，直接返回-1即可。
"""


# 包含重复元素的数组
def binary_search_insertion(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        m = (left + right) // 2
        if nums[m] < target:
            left = m + 1
        elif nums[m] > target:
            right = m - 1
        else:
            right = m - 1  # 首个小于 target 的元素在区间 [left, m-1] 中
    # 未找到 target ，返回插入点
    return left


def binary_search_left_edge(nums, target):
    idx = binary_search_insertion(nums, target)
    # 未找到 target ，返回 -1
    if idx == len(nums) or nums[idx] != target:
        return -1
    # 找到 target ，返回索引 i
    return idx


if __name__ == "__main__":
    # 包含重复元素的数组
    nums = [1, 3, 6, 6, 6, 6, 6, 10, 12, 15]
    # 二分查找左边界
    target = 6
    index = binary_search_left_edge(nums, target)
    print(f"最左一个元素 {target} 的索引为 {index}")


