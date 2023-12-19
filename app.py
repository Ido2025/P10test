from numbe import simp
from numbe import comp
import col
from icecream import ic


simp_called = False

def check_simp_called():
    if not simp_called:
        raise ImportError("Please call at least one function from the simp module before importing comp module.")

# call simp
result_add = simp.add_numbers(5, 10)
result_subtract = simp.subtract_numbers(10, 2)
simp_called = True

# call comp
check_simp_called() 
result_sum = comp.sum(156)
result_palin = comp.palin(445565544)

# call col
list1 = [5, 10, 15]
list2 = ['Ido', 'Gil', 'Yael']
zipped_result = col.myzip(list1, list2)

if __name__ == '__main__':

    # print simp
    print("Addition result:", result_add)
    print("Subtraction result:", result_subtract)

    ic("test")

    # print comp
    print("Sum of digits result:", result_sum)
    print("Is palindrome result:", result_palin)

    # print col
    print("Zipped Result:", zipped_result)
