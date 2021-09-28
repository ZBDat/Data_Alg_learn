import sys

if __name__ == "__main__":
    # 多行输入
    lines = sys.stdin.readlines()
    for line in lines:
        # strip 去回车 split 去空格
        nums = line.strip().split()
        for num in nums:
            print(int(num))
        print(nums)
