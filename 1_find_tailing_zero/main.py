"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:
    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        
        count = 0
        divisor = 5
        while number >= divisor:
            count += number // divisor
            divisor *= 5
        return count

s = Solution()

print(s.find_tailing_zeroes(7))
print(s.find_tailing_zeroes(10))
print(s.find_tailing_zeroes(25))
print(s.find_tailing_zeroes(100))
print(s.find_tailing_zeroes(-10))

