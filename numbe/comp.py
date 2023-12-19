from icecream import ic

#sum of number
def sum(number):
    number_str = str(abs(number))
    digit_sum = 0
    for digit in number_str:
        digit_sum += int(digit)
    return digit_sum

#palindrome
def palin(number):
    number_str = str(abs(number))
    reversed_str = ""
    for digit in number_str:
        reversed_str = digit + reversed_str
    return number_str == reversed_str

