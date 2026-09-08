def twosum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in seen:
            return [seen[comp], i]
        seen[num] = i
nums = [3,2,4]
target = 6
print(twosum(nums, target))

