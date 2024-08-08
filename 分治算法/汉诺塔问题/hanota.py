"""
给定三根柱子，记为 A、B 和 C 。起始状态下，柱子 A 上套着 n 个圆盘，它们从上到下按照从小到大的顺序排列。
我们的任务是要把这 n 个圆盘移到柱子 C 上，并保持它们的原有顺序不变。在移动圆盘的过程中，需要遵守以下规则。
1.圆盘只能从一根柱子顶部拿出，从另一根柱子顶部放入。
2.每次只能移动一个圆盘。
3.小圆盘必须时刻位于大圆盘之上。
"""

def move(src, tar):
    """移动一个圆盘"""
    # 从 src 顶部拿出一个圆盘
    pan = src.pop()
    # 将圆盘放入 tar 顶部
    tar.append(pan)
    

def dfs(i, src, buf, tar):
    # 若 src 只剩下一个圆盘，则直接将其移到 tar
    if i == 1:
        move(src, tar)
        return
    # 子问题 f(i-1) ：将 src 顶部 i-1 个圆盘借助 tar 移到 buf
    dfs(i - 1, src, tar, buf)
    # 子问题 f(1) ：将 src 剩余一个圆盘移到 tar
    move(src, tar)
    # 子问题 f(i-1) ：将 buf 顶部 i-1 个圆盘借助 src 移到 tar
    dfs(i - 1, buf, src, tar)


def solve_hanota(A, B, C):
    n = len(A)
    # 将 A 顶部 n 个圆盘借助 B 移到 C
    dfs(n, A, B, C)


if __name__ == "__main__":
    A = [5, 4, 3, 2, 1]
    B = []
    C = []
    print("初始状态下：")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")

    solve_hanota(A, B, C)

    print("圆盘移动完成后：")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")

