"""
冒泡排序（bubble sort）通过连续地比较与交换相邻元素实现排序。这个过程就像气泡从底部升到顶部一样，因此得名冒泡排序。

设数组的长度为 n ，冒泡排序的步骤:
首先，对 n - 1 个元素执行“冒泡”，将数组的最大元素交换至正确位置。
接下来，对剩余 n - 1 个元素执行“冒泡”，将第二大元素交换至正确位置。
以此类推，经过 n - 1 轮“冒泡”后，前 n - 1 大的元素都被交换至正确位置。
仅剩的一个元素必定是最小元素，无须排序，因此数组排序完成。
"""


def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]



if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    bubble_sort(nums)
    print("经过冒泡排序后nums为: ",nums)

