'''
Motivational print statements

def printRandom():
    quotes = {
    "you suck",
    "keep to business",
    "LOSER",
    "get better...fast",
    "it's not your fault you're dumb",
    "typing fast isn't typing well",
    "maybe you should quit",
    "lol that was horrible",
    "you hungry? you seem hungry"
        }
    return (id, random.choice(quotes))
'''

# def merge_sort(nums):
#     left = nums[:len(nums)//2]
#     right = nums[len(nums)//2:]
    
#     return merge(left, right)
    
# def merge(left, right):
#     if len(left) > 1 and not isSorted(left):
#         left = merge(left[:len(left//2)], left[len(left//2):])
#     if len(right) > 1 and not isSorted(right):
#         right = merge(right[:len(left//2)], right[len(left//2):])
    
# def isSorted(nums):
#     for i in range(len(nums)):
#         if nums[i] > nums[i+1]:
#             return False
#     return True

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot  =  nums[len(nums)//2]
    left   = [number for number in nums if number <  pivot]
    right  = [number for number in nums if number >  pivot]
    middle = [number for number in nums if number == pivot]
    #thank you Ryan
   

    left = merge_sort(left)
    right = merge_sort(right)
    

    return left + middle + right


print(merge_sort([5,4,3,2,1]))