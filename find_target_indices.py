def targetIndices(nums,target):
    res=[]
    nums.sort()
    for i in range(len(nums)):
        if nums[i]==target:
            res.append(i)
    return res
nums=[1,2,5,2,3]
target=5
ans = targetIndices(nums,target)
print(ans)
