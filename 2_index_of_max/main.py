"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if not numbers:
            return "list can not blank"
        
        max_index = 0
        max_value = numbers[0]
        
        for i in range(1, len(numbers)):
            if numbers[i] > max_value:
                max_value = numbers[i]
                max_index = i
                
        return max_index

s = Solution()

print(s.find_max_index([1, 2, 1, 3, 5, 6, 4]))
print(s.find_max_index([10, 9, 8, 11, 2]))
print(s.find_max_index([]))
print(s.find_max_index([-10, -3, -20, -1]))
