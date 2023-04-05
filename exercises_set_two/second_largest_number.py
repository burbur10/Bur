def second_largest(numbers):
    largest = second_largest  = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest
numbers = [2, 5, 7, 13, 8, 29, 20, 39]
second_largest_number = second_largest(numbers)
print(second_largest_number)