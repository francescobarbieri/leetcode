from re import sub


# Solution 1

def twoSumFirst(nums, target):
    output = []

    for idx, x in enumerate(nums):
        for idy, y in enumerate(nums):
            if idx != idy:
                if x + y == target:
                    output = [idy, idx]

    return output

#print(twoSumFisrt([3, 3], target = 6))

# Solution 2:
def twoSum(nums, target):
    dictionary = {}
    output = []

    for idx, x in enumerate(nums):
        required = target - x
        if required in dictionary:
            output = [dictionary[required], idx]
            break
        dictionary[x] = idx
    return output

print(twoSum([3, 3, 9], target = 6))