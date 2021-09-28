def moveZeroes1(nums) -> None:
    # 不保序
    left = 0
    right = len(nums)-1
    while left <= right:
        if nums[left] == 0:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                continue
        else:
            left += 1


def moveZeroes2(nums) -> None:
    # 记载非零元位置，逐个填入之后补零。
    # 不需担心覆盖，因为非零元个数小于等于整个数组大小
    l = len(nums)
    none_zero_idx = []
    for p in range(l):
        if nums[p] != 0:
            none_zero_idx.append(p)
    for i in range(len(none_zero_idx)):
        nums[i] = nums[none_zero_idx[i]]
    for j in range(len(none_zero_idx), l):
        nums[j] = 0


def moveZeroes3(nums) -> None:
    # 无需额外数组。双指针一个处理零元一个处理非零
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    moveZeroes2(nums)
    print(nums)