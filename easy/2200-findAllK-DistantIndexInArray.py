# Solution

def findKDistantIndices(nums, key, k):
    output = []
    kIndexes = []

    for idx, x in enumerate(nums):
        if x == key:
            kIndexes.append(idx)
    
    for idx, x in enumerate(nums):
        for y in kIndexes:
            if abs(idx - y) <= k and nums[y] == key:
                output.append(idx)
                break

    return output

print(findKDistantIndices([2,2,2,2,2], 2, 2))