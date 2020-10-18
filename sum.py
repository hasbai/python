def twoSum(nums, target):
    hashmap = {}
    result = []        
    for i in range(0,len(nums)):
        hashmap[nums[i]]=i
    for i in range(0,len(nums)):
        a = target - nums[i]
        j = hashmap.get(a)
        if j is None or j <= i :
            continue
        else:
            result.append([i,j])
    return result

def threeSum(nums):
    result = []
    for i in range(0,len(nums)):
        for two_result in twoSum(nums,-nums[i]):
            if i <= two_result[1]:
                continue
            else:
                t = two_result[:]
                t1 = t.append(i)
                result.append(t)
    return result

nums = [7,-3,-4,-3]
print(threeSum(nums))
