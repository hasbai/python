'''
given an array and return all the lists of index that satisfy: 
    twoSum: two number's sum equals to a given number
    threeSum: three number's sum equels to 0
using hashmap to locate the needed index of number, reducing the time conplexity of twoSum to O(n^2)
'''
def fillHashmapRepeatedly (nums,hashmap={}):
    for i in range(0,len(nums)):
        if nums[i] in hashmap :
            hashmap[nums[i]].append(i)
        else :
            hashmap[nums[i]] = [i]
    return hashmap

def twoSum(nums, target):
    result = []        
    for i in range(0,len(nums)):
        second_number = target - nums[i]
        locationList = hashmap.get(second_number)
        if locationList is None:
            continue
        else :
            for location in locationList:
                if location <= i :
                    continue
                else :
                    result.append([i,location])
    return result

def threeSum(nums):
    result = []
    for i in range(0,len(nums)):
        for two_result in twoSum(nums,-nums[i]):
            if i <= two_result[1]:
                continue
            else:
                t = two_result[:]
                t.append(i)
                result.append(t)
    return result

nums = [7,-3,-4,-3,5,489,114514,0,-486]
hashmap = fillHashmapRepeatedly(nums)
print(threeSum(nums))
