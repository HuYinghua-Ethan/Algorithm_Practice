"""
Question:
给定一个整数数组 nums 和一个目标元素 target ，请在数组中搜索“和”为 target 的两个元素，并返回它们的数组索引。返回任意一个解即可。
"""

# 以时间换空间 暴力枚举
def two_sum_brute_force(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i, j]


# 以空间换时间
def two_sum_hash_table(nums, target):
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] in dict:
            return [dict[target - nums[i]], i]
        dict[nums[i]] = i



if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 13
    res1 = two_sum_brute_force(nums, target)
    res2 = two_sum_hash_table(nums, target)
    print("两个数的数组索引为:", res1)
    print("两个数的数组索引为:", res2)


