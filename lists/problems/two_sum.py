
# Question 2 - Find pairs
# Leetcode - Two Sum

#brute force, n^2 time complexity

def two_sum(nums, target): 
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i,j)

myList = [1,2,3,2,3,4,5,6]

two_sum(myList, 6)


# most efficient solution, time complexity = O(n)

def two_sum(nums, target):
    hm = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in hm:
            return [ hm[complement], i]
    
        hm[num] = i

nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")