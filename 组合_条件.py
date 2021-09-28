import sys


def insert_pos(nums, target):
    pos = 0
    r = len(nums) - 1
    while pos <= r:
        mid = pos + (r - pos) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            pos = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return pos


def select(l):
    l.sort(key=lambda x: (x[0], -x[1]))
    tails = []
    for k in range(len(l)):
        if not tails or l[k][1] > tails[-1]:
            tails.append(l[k][1])
        else:
            pos = insert_pos(tails, l[k][1])
            tails[pos] = l[k][1]
    return len(tails)


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    T = int(lines[0].strip())
    index = 1
    while index < (2*T + 1):
        n = int(lines[index].strip())
        xs = [int(x) for x in lines[index+1].strip().split()]
        ys = [int(y) for y in lines[index+2].strip().split()]
        l = []
        for i in range(len(xs)):
            l.append([xs[i], ys[i]])
        print(select(l))
        index += 3
