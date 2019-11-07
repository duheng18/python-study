'''
对下面测试方法使用pytest的rerun, 参数化方法来实现自动化测试
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return random.choice([nums, None, 10])

'''
import pytest
import random

data = [([1, 2, 3, 4], [1, 2, 3, 4]), ([4, 5, 6,7], [4, 7, 6,5])]


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return random.choice([nums, None, 10])


def bubble_sort_new(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


@pytest.mark.flaky(reruns=3,reruns_delay=2)
@pytest.mark.parametrize("nums", data)
def test_bubble_sort(nums):
    print(bubble_sort(nums))
    print(bubble_sort_new(nums))
    assert bubble_sort(nums) == bubble_sort_new(nums)


if __name__ == '__main__':
    pytest.main()
