"""
Question:
给定一个长度为 n 的有序数组 nums ，其中所有元素都是唯一的，请查找元素 target 。

从分治角度，我们将搜索区间 [i, j] 对应的子问题记为 f(x, j) 。
以原问题 f(0, n - 1) 为起始点，通过以下步骤进行二分查找。
1.计算搜索区间[i, j]的中点 m ，根据它排除一半搜索区间。
2.递归求解规模减小一半的子问题，可能为 f(i, m - 1)或 f(m + 1, j)。
3.循环第 1. 步和第 2. 步，直至找到 target 或区间为空时返回。
"""



def dfs(nums, i, j,target):
    if i > j:  #  # 若区间为空，代表无目标元素，则返回 -1
        return -1
    mid = (i + j) // 2
    if nums[mid] < target:  # 递归子问题 f(m+1, j)
        return dfs(nums, mid + 1, j, target)
    elif nums[mid] > target:  # 递归子问题 f(i, m-1)
        return dfs(nums, i, mid - 1, target)
    else:
        return mid  # 找到目标元素，返回其索引



if __name__ == "__main__":
    nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]
    target = 6
    index = dfs(nums, 0, len(nums)-1, target)
    print("经过二分查找后 target 的 index 为: ", index)
    
