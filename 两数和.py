def twoSum1(numbers, target):
    result = []
    for left in range(len(numbers)):
        for right in range(left + 1, len(numbers)):
            if numbers[left] + numbers[right] == target:
                result.append(left)
                result.append(right)
    return result


def twoSum2(numbers, target: int):
    # 需要利用“有序”条件，否则会超时
    left = 0
    right = len(numbers)-1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
    return None


if __name__ == "__main__":
    result = twoSum2([2, 7, 11, 15], 9)
    print(result)