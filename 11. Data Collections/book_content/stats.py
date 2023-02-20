from math import sqrt


def getNumbers() -> list:
    nums = []

    xStr = input("Enter a number(<Enter> to quit)>> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)
        xStr = input("Enter a number (<Enter> to quit)>> ")
    return nums


def mean(nums) -> float:
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)


def meanStdDev(nums) -> tuple:
    sumDevSq = 0.0
    total = 0
    for num in nums:
        total = total + num
        mean = total / len(nums)
        dev = mean - num
        sumDevSq = sumDevSq + dev * dev
    mean_return = total / len(nums)
    std_return = sqrt(sumDevSq / (len(nums) - 1))

    return mean_return, std_return


def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        med = (nums[midPos] + nums[midPos - 1]) / 2
    else:
        med = nums[midPos]
    return med


def main():
    print("This program computes mean, median, and standard deviation.")

    data = getNumbers()
    med = median(data)
    mean_std = meanStdDev(data)

    print("The median is", med)
    print(f"The mean {mean_std[0]} and standard deviation {mean_std[1]}")


if __name__ == '__main__':
    main()
