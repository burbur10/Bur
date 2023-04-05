def second_least_num(numbers):
    least = second_least = float('inf')
    for n in numbers:
        if n < least:
            second_least = least
            least = n   
        elif n < second_least:
            second_least = n
    return second_least
numbers = [1, 2, 3, 4, 5]
second_least = second_least_num(numbers)
print(second_least)