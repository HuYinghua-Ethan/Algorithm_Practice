""""
插入排序（insertion sort）是一种简单的排序算法，它的工作原理与手动整理一副牌的过程非常相似。

具体来说，我们在未排序区间选择一个基准元素，将该元素与其左侧已排序区间的元素逐一比较大小，并将该元素插入到正确的位置。

插入排序的整体流程:
初始状态下，数组的第 1 个元素已完成排序。
选取数组的第 2 个元素作为 base ，将其插入到正确位置后，数组的前 2 个元素已排序。
选取第 3 个元素作为 base ，将其插入到正确位置后，数组的前 3 个元素已排序。
以此类推，在最后一轮中，选取最后一个元素作为 base ，将其插入到正确位置后，所有元素均已排序。
"""


def insertion_sort(nums):
    n = len(nums)
    # 从第二个数开始
    for i in range(1, n):
        base = nums[i]
        j = i - 1
        while j >= 0 and base < nums[j]:
            nums[j+1] = nums[j]  # 将 nums[j] 向右移动一位
            j -= 1
        nums[j + 1] = base  # 将 base 赋值到正确位置           

    

if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    insertion_sort(nums)
    print("经过插入排序后：", nums)

