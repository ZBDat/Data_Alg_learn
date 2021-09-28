from typing import List


def explore(grid: List[List[int]], i, j):
    """
    输入的节点坐标i，j。只在该节点是陆地时才运行这个函数
    """
    # 退出条件：超过范围或碰到0
    if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 1:
        return 0
    grid[i][j] = 0  # 重点：将探索过的节点置零防止重复
    ans = 1
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ans += explore(grid, i + di, j + dj)
    return ans


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    ans = 0
    for i, l in enumerate(grid):  # 一个遍历二维的用法
        for j, n in enumerate(l):
            ans = max(explore(grid, i, j), ans)
    return ans


if __name__ == "__main__":
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(maxAreaOfIsland(grid=grid))
