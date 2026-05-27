def subset_sum_to_target(input_set, target_sum):
    nums = list(input_set)
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target_sum:
                result.append({nums[i], nums[j]})

    return result


input_set = {2, 4, 5, 7, 8}
target_sum = 10

print(subset_sum_to_target(input_set, target_sum))