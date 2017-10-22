def twoSum(nums,target):
    if len(nums)<=1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]],i]
        else:
            buff_dict[target-nums[i]] = i
nums = [2,7,11,15]
target = 18
a = twoSum(nums,target)
print(a)