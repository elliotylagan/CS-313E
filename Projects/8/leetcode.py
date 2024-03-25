# Name 1: Ryan Schlimme
# EID 1: rjs4499

# Name 2: Elliot Ylagan
# EID 2:EPY82

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for i in range(len(nums)):
            if target - nums[i] in hasher.keys():
                return [i, hasher[target - nums[i]]]
            else:
                hasher[nums[i]] = i


    def letterCombinations(self, digits: str) -> List[str]:
        letter_combo = ["", "", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        result = []
        temp = []
        if len(digits) > 0:
            self.helper(result, temp, letter_combo, digits, 0)
        return result

    def helper(self, result, temp, letter_combo, digits, index):
        if len(temp) == len(digits):
            result.append("".join(temp))
            return
        
    
        for letter in letter_combo[int(digits[index])]:
            if letter not in temp:
                temp.append(letter)
                self.helper(result, temp, letter_combo, digits, index+1)
                temp.pop(len(temp)-1)


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = None
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = prev
        return temp


    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        upper = len(letters) - 1
        lower = 0
        mid = (upper + lower) // 2
        if target > letters[upper]: #must have a possible solution
            return letters[0]
        while upper > lower and mid > 0:
            mid = (upper + lower) // 2
            if target < letters[mid]:
                upper = mid
            if target > letters[mid]:
                lower = mid
            if letters[mid] > target and letters[mid -1] <= target: #is smallest option greater than target
                return letters[mid]
        return letters[0]

    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        answer = []

        for i in range(0, len(nums), 2):
            answer.append(nums[i + 1])
            answer.append(nums[i])
        
        return answer
    
def sorted(nums):
    if len(nums) < 2:
        return nums
    
    left =   []
    middle = []
    right =  []

    pivot = nums[3]
    for number in nums:
        if number <  pivot:
            left.append(number)
        if number == pivot:
            middle.append(number)
        if number >  pivot: 
            right.append(number)

    left = sorted(left)
    right = sorted(right)

    return left + middle + right
