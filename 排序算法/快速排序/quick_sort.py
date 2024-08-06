"""
快速排序（quick sort）是一种基于分治策略的排序算法，运行高效，应用广泛。
快速排序的核心操作是“哨兵划分”，其目标是：选择数组中的某个元素作为“基准数”，将所有小于基准数的元素移到其左侧，而大于基准数的元素移到其右侧。

哨兵划分的流程步骤：
1.选取数组最左端元素作为基准数，初始化两个指针 i 和 j 分别指向数组的两端。
2.设置一个循环，在每轮中使用 i(j)分别寻找第一个比基准数大（小）的元素，然后交换这两个元素。
3.循环执行步骤2.，直到 i 和 j 相遇时停止，最后将基准数交换至两个子数组的分界线。
哨兵划分完成后，原数组被划分成三部分：左子数组、基准数、右子数组，且满足“左子数组任意元素 <= 基准数 <= 右子数组任意元素”。因此，我们接下来只需对这两个子数组进行排序。

快速排序的整体流程:
1.首先对原数组执行一次“哨兵划分”，得到未排序的左子数组和右子数组。
2.然后，对左子数组和右子数组分别递归执行“哨兵划分”。
3.持续递归，直至子数组长度为1时终止，从而完成整个数组的排序。

基准数优化
快速排序在某些输入下的时间效率可能降低。举一个极端例子，假设输入数组是完全倒序的，由于我们选择最左端元素作为基准数，那么在哨兵划分完成后，基准数被交换至数组最右端，导致左子数组长度为 n - 1、右子数组长度为 0。
如此递归下去，每轮哨兵划分后都有一个子数组的长度为 0，分治策略失效，快速排序退化为“冒泡排序”的近似形式。
为了尽量避免这种情况发生，我们可以优化哨兵划分中的基准数的选取策略。为了进一步改进，我们可以在数组中选取三个候选元素（通常为数组的首、尾、中点元素），并将这三个候选元素的中位数作为基准数。

尾递归优化
在某些输入下，快速排序可能占用空间较多。以完全有序的输入数组为例，设递归中的子数组长度为 m ，每轮哨兵划分操作都将产生长度为 0 的左子数组和长度为 m - 1 的右子数组，这意味着每一层递归调用减少的问题规模非常小（只减少一个元素），递归树的高度会达到 n - 1，此时需要占用 O(n)大小的栈帧空间。
为了防止栈帧空间的累积，我们可以在每轮哨兵排序完成后，比较两个子数组的长度，仅对较短的子数组进行递归。
"""

def median_three(nums, left, mid, right):
    l, m, r = nums[left], nums[mid], nums[right]
    if l <= m <= r or r <= m <= l:
        return mid
    elif m <= l <= r or r <= l <= m:
        return left
    else:
        return right


# 哨兵划分的实质是将一个较长数组的排序问题简化为两个较短数组的排序问题。
def partition(nums, left, right):
    i, j = left, right
    med = median_three(nums, left, (left + right) // 2, right)
    nums[left], nums[med] = nums[med], nums[left]   # 将基准数移至数组左端
    while i < j:
        while i < j and nums[j] >= nums[left]:  # 从右向左找首个小于基准数的元素
            j -= 1
        while i < j and nums[i] <= nums[left]:  # 从右向左找首个大于基准数的元素
            i += 1
        nums[i], nums[j] = nums[j], nums[i]     # 交换这两个元素
    nums[left], nums[i] = nums[i], nums[left]   # 将基准数移至两子数组的分界线
    # 返回基准数的索引
    return i   
            

def quick_sort(nums, left, right):
    if left >= right:
        return
    # 先执行一次哨兵划分
    pivot = partition(nums, left, right)
    # 对左子数组递归执行哨兵划分
    partition(nums, left, pivot - 1)
    # 对右子数组递归执行哨兵划分
    partition(nums, pivot + 1, right)


def quick_sort_optimize(nums, left, right):
    # 子数组长度为1时终止
    while left < right:
        pivot = partition(nums, left, right)
        # 在每轮哨兵排序完成后，比较两个子数组的长度，仅对较短的子数组进行递归
        if pivot - left < right - pivot:
            quick_sort_optimize(nums, left, pivot - 1)
            left = pivot + 1
        else:
            quick_sort_optimize(nums, pivot + 1, right)
            right = pivot - 1


if __name__ == "__main__":
    nums = [2, 4, 1, 0, 3, 5]
    # partition(nums, 0, len(nums) - 1)
    # print("哨兵划分完成后 nums =", nums)
    quick_sort(nums, 0, len(nums) - 1)
    print("快速排序完成后 nums =", nums)
    quick_sort_optimize(nums, 0, len(nums) - 1)
    print("优化后的快速排序完成后 nums =", nums)







