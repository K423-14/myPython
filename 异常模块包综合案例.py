# from my_module import *
# print(my_module.test(1, 2))
# print(test_a(1, 2))
# print(test_b(1, 2))

from my_utils import file_util
from my_utils import str_util

print(str_util.str_reverse("hello"))
print(str_util.substr("hello", 1, 3))

file_util.append_to_file("bill.txt", "hello")
file_util.print_file_info("bill.txt")


