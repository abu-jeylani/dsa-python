
# Leetcode question 217
def contains_duplicate(nums):
    #use a hashset to store nums we come across
    hash_set = set()

    for num in nums:
        # check if number is in hashset
        if num in hash_set:
            return True
        hash_set.add(num)

    return False

print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3]))