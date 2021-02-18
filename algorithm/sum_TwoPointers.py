def twoSum(nums,target):
 #   nums.sort()
    result_list = []
    i = 0
    j = len(nums)-1
    while i < j :
        s = nums[i] + nums[j]
        if s == target:
            result_list.append([i,j])
            i = i+1
        elif s > target:
            j=j-1
        else:
            i=i+1
    return(result_list)
def threeSum(nums):
    result = set()
    result_list = []
    if len(nums) <= 2:
        return []
    else:
        nums.sort()
        for i in range (0,nums.count(0)-3):
            nums.remove(0)
        for k in range(0,len(nums)):
            two_result_list = twoSum(nums,-nums[k])
            if len(two_result_list) == 0:
                continue
            else:
                for two_result in two_result_list:
                    if two_result is None or two_result[0]==k or two_result[1]==k:
                        continue
                    else:
                        three_result = [nums[k],nums[two_result[0]],nums[two_result[1]]]
                        three_result.sort()
                        tup = tuple(three_result)
                        result.add(tup)
    for t in result :
        t = list(t)
        result_list.append(t)
    return result_list

    

nums = [3,0,-2,-1,1,2]
print(threeSum(nums))