from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # head = nums[-k:]
    # back = nums[:len(nums) - k]
    #
    # for i in range(len(head)):
    #     nums[i] = head[i]
    #
    # for i in range(len(back)):
    #     nums[i + k] = back[i]
    m = k % len(nums)
    nums[-m:].reverse()


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    print(nums)
