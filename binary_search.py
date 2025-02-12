def search(nums, target: int) -> int:
    if len(nums) == 0:
        return -1

    middle = len(nums) // 2
    print(middle)
    print(nums)
    if nums[middle] == target:
        return middle
    if target > nums[middle]:
        search(nums[middle+1:], target)
    if target < nums[middle]:
        search(nums[:middle + 1], target)


        

nums = [1, 2, 3, 4, 5]
target = 4
print("search(nums, target): ", search(nums, target))