def _number(numbers):
    smallest =numbers[0]
        
    for num in numbers:
        if num<smallest:
    
            smallest = num
        
    return smallest
numbers = [2, 5, 7, 13, 8, 29, 0, 39]
smallest = _number(numbers)
print(smallest)