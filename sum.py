# takes input from you.
numbers = []

# Gets the 10 numbers
for i in range(10):
    number = int(input(f"Enter number {i+1} (consecutive number): "))
    numbers.append(number)

#Compute the sum of all the numbers
sum_all_numbers = sum(numbers)
print(f"\nSum of all numbers: {sum_all_numbers}")

#separate even from odd and ad dall together.
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

sum_even = sum(even_numbers)
sum_odd = sum(odd_numbers)

print(f"\nEven numbers: {even_numbers}")
print(f"Sum of even numbers: {sum_even}")

print(f"\nOdd numbers: {odd_numbers}")
print(f"Sum of odd numbers: {sum_odd}")