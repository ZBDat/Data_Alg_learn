from collections import deque


def drone_maze(matrix):
    n, m = len(matrix), len(matrix[0])
    # define the starting point
    si, sj = 0, 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'S':
                si, sj = i, j
                break

    # BFS
    q = deque()
    q.append((si, sj, 0, 5))
    seen = {(si, sj)}
    while q:
        i, j, step, count = q.popleft()

        if matrix[i][j] == 'E':
            return step

        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] != '#' and (ni, nj) not in seen:
                q.append((ni, nj, step+1, count))
                seen.add((ni, nj, step+1, count))
        flyi, flyj = n-i-1, m-j-1
        if 0 <= flyi < n and 0 <= flyj < m and matrix[flyi][flyj] != '#' and count and (flyi, flyj) not in seen:
            q.append((flyi, flyj, step+1, count-1))
            seen.add((flyi, flyj, step+1, count-1))

    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(input().split()))

    print(drone_maze(matrix))
