
#leetcode 268
'''

'''
def missing_number(nums: list[int]):
        
        correctSum = len(nums)
        resultingSum = 0

        for i in range(len(nums)):
            correctSum += i
        for i in nums:
            resultingSum +=  i
        return correctSum - resultingSum

print(missing_number([0,1,2,4,5]))