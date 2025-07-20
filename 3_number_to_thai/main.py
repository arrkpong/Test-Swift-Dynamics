"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number == 0:
            return "ศูนย์"

        num_text = ""
        units = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        digits = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]

        def convert_segment(n):
            result = ""
            n_str = str(n)
            length = len(n_str)

            for i, digit_char in enumerate(n_str):
                digit = int(digit_char)
                pos = length - i - 1

                if digit == 0:
                    continue
                if pos == 0:
                    if digit == 1 and length > 1:
                        result += "เอ็ด"
                    else:
                        result += digits[digit]
                elif pos == 1:
                    if digit == 1:
                        result += "สิบ"
                    elif digit == 2:
                        result += "ยี่สิบ"
                    else:
                        result += digits[digit] + "สิบ"
                else:
                    result += digits[digit] + units[pos]
            return result

        num_str = str(number)
        if len(num_str) > 7:
            return "number out of range"

        if number >= 1_000_000:
            millions = number // 1_000_000
            remainder = number % 1_000_000
            num_text += convert_segment(millions) + "ล้าน"
            if remainder > 0:
                num_text += convert_segment(remainder)
        else:
            num_text += convert_segment(number)

        return num_text

s = Solution()

print(s.number_to_thai(101))
print(s.number_to_thai(21))
print(s.number_to_thai(10))
print(s.number_to_thai(1000000))
print(s.number_to_thai(1002001))
print(s.number_to_thai(0))
print(s.number_to_thai(-1))
