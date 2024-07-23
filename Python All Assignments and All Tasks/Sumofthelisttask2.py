def list_operations(nums):
    total = 0
    maximum = nums[0]
    for num in nums:
        total += num
        if num > maximum:
            maximum = num
    return total, maximum


input_str = input("Enter a list of numbers separated by spaces: ")
input_list = input_str.split()
nums = list(map(int, input_list))


sum_result, max_result = list_operations(nums)


print(f"Sum of the list: {sum_result}")
print(f"Maximum of the list: {max_result}")
