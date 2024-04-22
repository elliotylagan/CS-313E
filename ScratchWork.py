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
def subsets(nums):
    def helper(result, subset, i, nums):
        if i == len(nums):
            result.append(subset[:])
            return
        helper(result, subset, i + 1, nums)
        subset.append(nums[i])
        helper(result, subset, i + 1, nums)
        subset.pop(len(subset) - 1)
    result = []
    subset = []
    helper(result, subset, 0, nums)
    return result

print(subsets([1, 2, 3, 4]))
