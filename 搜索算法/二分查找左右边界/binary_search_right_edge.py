""""
Question:
给定一个长度为 n 的有序数组 nums ，其中可能包含重复元素。请返回数组中最右一个元素 target 的索引。若数组中不包含该元素，则返回-1。


转化为查找元素
我们知道，当数组不包含 target 时，最终 left和 right 会分别指向首个大于、小于 target 的元素。
因此，如图 10-8 所示，我们可以构造一个数组中不存在的元素，用于查找左右边界。
查找最左一个 target ：可以转化为查找 target - 0.5 ，并返回指针 left。
查找最右一个 target ：可以转化为查找 target + 0.5 ，并返回指针 right。

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
            left = m + 1  # 最右边的 target 在区间 [m +1, right] 中
    # 未找到 target ，返回插入点
    return right


def binary_search_right_edge(nums, target):
    idx = binary_search_insertion(nums, target)
    # 未找到 target ，返回 -1
    if idx == -1 or nums[idx] != target:
        return -1
    # 找到 target ，返回索引 i
    return idx


if __name__ == "__main__":
    # 包含重复元素的数组
    # nums = [1, 3, 4, 6, 6, 6, 6, 10, 12, 15]
    nums = [7, 8, 9, 10, 11, 12, 13]
    # nums = [1, 2, 3, 4, 5]
    # 二分查找右边界
    target = 6
    index = binary_search_right_edge(nums, target)
    print(f"最右一个元素 {target} 的索引为 {index}")


# 另一种思想：
# # 包含重复元素的数组
# def binary_search_insertion(nums, target):
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         m = (left + right) // 2
#         if nums[m] < target:
#             left = m + 1
#         elif nums[m] > target:
#             right = m - 1
#         else:
#             right = m - 1  # 首个小于 target 的元素在区间 [left, m-1] 中
#     # 未找到 target ，返回插入点
#     return left


# def binary_search_right_edge(nums: list[int], target: int) -> int:
#     """二分查找最右一个 target"""
#     # 转化为查找最左一个 target + 1
#     i = binary_search_insertion(nums, target + 1)
#     # j 指向最右一个 target ，i 指向首个大于 target 的元素
#     j = i - 1
#     # 未找到 target ，返回 -1
#     if j == -1 or nums[j] != target:
#         return -1
#     # 找到 target ，返回索引 j
#     return j


# if __name__ == "__main__":
#     # 包含重复元素的数组
#     nums = [1, 3, 6, 6, 6, 6, 6, 10, 12, 15]
#     # 二分查找左边界
#     target = 6
#     index = binary_search_right_edge(nums, target)
#     print(f"最左一个元素 {target} 的索引为 {index}")


