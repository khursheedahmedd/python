

def TwoSum(sum, nums):
    i =0
    while(i < len(nums)):
        j = i+1
        while(j< len(nums)):
            if(sum == (nums[i] + nums[j])):
                return 'Yes'
            j += 1
        i+=1
    return 'No'

nums = [4, 2, 7,3, 9]

sum = 16

print(TwoSum(sum, nums))