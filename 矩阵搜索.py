# 给出矩阵中所有元素离最近的零的距离
import collections
from typing import List


def updateMatrix(matrix: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])
    dist = [[0] * n for _ in range(m)]
    zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
    # 将所有的 0 添加进初始队列中
    q = collections.deque(zeroes_pos)
    seen = set(zeroes_pos)

    # 广度优先搜索
    while q:
        i, j = q.popleft()
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
                seen.add((ni, nj))

    return dist


def orangesRotting(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    pos = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2]
    rot = collections.deque(pos)
    fresh = sum([l.count(1) for l in grid])

    round = 0
    while fresh and rot:
        round += 1
        for _ in range(len(rot)):
            i, j = rot.popleft()
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] == 1:
                    grid[i + di][j + dj] = 2
                    rot.append((i + di, j + dj))
                    fresh -= 1

    if fresh > 0:
        return -1

    return round


if __name__ == "__main__":
    mat = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    ans = orangesRotting(mat)
    print(ans)
