数组不包含 target 时，最终 left和 right 会分别指向首个大于、小于 target 的元素。
因此，如图 10-8 所示，我们可以构造一个数组中不存在的元素，用于查找左右边界。
查找最左一个 target ：可以转化为查找 target - 0.5 ，并返回指针 left。
查找最右一个 target ：可以转化为查找 target + 0.5 ，并返回指针 right。
