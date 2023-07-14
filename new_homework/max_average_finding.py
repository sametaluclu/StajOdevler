def max_average_subarray_find(nums):
    if not nums:
        return []

    max_average = float("-inf")
    start_index = 0
    end_index = 0

    for i in range(len(nums)):
        total = nums[i]
        for j in range(i+1, len(nums)):
            total += nums[j]
            average = total / (j - i + 1)
            if average > max_average:
                max_average = average
                start_index = i
                end_index = j

    return nums[start_index: end_index + 1]

nums1 = [2, -1, 3, -4, 2, 5, -2, 1]
nums2 = [1, -2, 3, -1, 2, -3, 4, -1]

max_average_subarray1 = max_average_subarray_find(nums1)
average1 = sum(max_average_subarray1) / len(max_average_subarray1)
print("Çıktı 1:", max_average_subarray1, "(Ortalama 1:", average1, ")")

max_average_subarray2 = max_average_subarray_find(nums2)
average2 = sum(max_average_subarray2) / len(max_average_subarray2)
print("Çıktı 2:", max_average_subarray2, "(Ortalama 2:", average2, ")")
