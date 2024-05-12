from task_1 import how_many_computers
from task_2 import common_divisors
from task_3 import prime_numbers
from task_4 import multiplication_table

for i in range(-1, 50):
    print(how_many_computers(i))

print(common_divisors([4, 15, 20]))
print(common_divisors([6, 12, 48]))
print(common_divisors([1, 7]))
print(common_divisors([5, 15, 21]))
print(common_divisors([8, 16, 24]))

print(prime_numbers(11, 20))
print(prime_numbers(0, 10))
print(prime_numbers(-5, 15))
print(prime_numbers(15, -5))
print(prime_numbers(-5, 1))

multiplication_table(2)
multiplication_table(5)
multiplication_table(8)
multiplication_table(10)
