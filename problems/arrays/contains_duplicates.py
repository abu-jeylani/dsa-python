
def contains_duplicate(nums):
    # TODO
    seen = set()
    for num in nums: 
        if num in seen:
            return True
        seen.add(num)
    return False



nums = [1,2,3,1]
contains_duplicate(nums)
