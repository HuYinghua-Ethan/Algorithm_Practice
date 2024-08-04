"""
Question:
给定一个长度为 n 的有序数组 nums 和一个元素 target ，数组不存在重复元素。
现将 target 插入数组 nums 中，并保持其有序性。
若数组中已存在元素 target ，则插入到其左方。请返回插入后 target 在数组中的索引。

一.无重复元素的情况
先想清楚两个问题：
问题一：当数组中包含 target 时，插入点的索引是否是该元素的索引？
假设数组中存在多个 target ，则普通二分查找只能返回其中一个 target 的索引，而无法确定该元素的左边和右边还有多少 target。
题目要求将 target 插入到相等元素的左边，这意味着新插入的 target 替换了原来 target 的位置。也就是说，当数组包含 target 时，插入点的索引就是该 target 的索引。

问题二：当数组中不存在 target 时，插入点是哪个元素的索引？
当 nums[m] < target 时 left 移动，这意味着 left 在向大于等于 target 的元素靠近。同理，right 始终在向小于等于 target 的元素靠近。
因此，二分结束时一定有：left 指向首个大于 target 的元素， right 指向首个小于 target 的元素。易得当数组不包含 target 时，插入点的索引是 left 的索引。


二.存在重复元素
假设数组中存在多个 target ，则普通二分查找只能返回其中一个 target 的索引，而无法确定该元素的左边和右边还有多少个 target。
题目要求将 target 插入到相等元素的左边，所以我们需要查找数组中最左一个 target 的索引。
初步实现步骤：
1.执行二分查找，得到任意一个 target 的索引，记为 k。
2.从索引 k 开始，向左进行线性遍历，当找到最左边的 target 时返回。
此方法虽然可用，但其包含线性查找，因此时间复杂度为 O(n)。当数组中存在很多重复的 target 时，该方法效率很低。

拓展二分查找代码
整体流程保持不变，每轮先计算中点索引 m ，再判断 target 和 nums[m] 的大小关系，分为以下几种情况：
1.当 nums[m] < target 或 nums[m] > target 时，说明还没有找到 target ，因此采用普通二分查找的缩小区间操作，从而使指针 left 和 right 向 target 靠近。
2.当 nums[m] == target 时，说明小于 target 的元素在区间[left, m - 1]中，因此采用 right = m - 1 来缩小区间，从而使指针 right 向小于 target 的元素靠近。

循环完成后，left 指向最左边的 target , right 指向首个小于 target 的元素，因此 left 就是插入点的索引
""" 


# 无重复元素的情况
def binary_search_insertion_sample(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        m = (left + right) // 2
        if nums[m] < target:
            left = m + 1
        elif nums[m] > target:
            right = m - 1
        else:
            return m
    # 未找到 target ，返回插入点
    return left


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
            right = m - 1  # 首个小于 target 的元素在区间 [i, m-1] 中
    # 未找到 target ，返回插入点
    return left


if __name__ == "__main__":
    # 无重复元素的数组
    print("无重复元素的数组的情况")
    nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]
    target = 6
    idx = binary_search_insertion_sample(nums, target)
    print(f"元素 {target} 的插入点的索引为 {idx}")

    print("-------------------------------------")

    # 包含重复元素的数组
    print("包含重复元素的数组的情况")
    nums = [1, 3, 6, 6, 6, 6, 6, 10, 12, 15]
    idx = binary_search_insertion(nums, target)
    print(f"元素 {target} 的插入点的索引为 {idx}")


