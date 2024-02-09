def convert_base(number, from_base, to_base):
    if from_base < 2 or to_base < 2:
        raise ValueError("Base must be greater than or equal to 2")

    decimal_number = 0
    for i, digit in enumerate(reversed(str(number))):
        decimal_number += int(digit) * (from_base ** i)

    result = ""
    while decimal_number > 0:
        remainder = decimal_number % to_base
        result = str(remainder) + result
        decimal_number //= to_base

    return result if result else "0"

number = int(input("Enter the number: "))
from_base = int(input("Enter the base of the number: "))
to_base = int(input("Enter the base to convert to: "))

result = convert_base(number, from_base, to_base)
print(f"{number} in base {from_base} is {result} in base {to_base}")
