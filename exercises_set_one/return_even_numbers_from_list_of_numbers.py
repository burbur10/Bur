def number_of_even_nmbers(numbers):

    even_numbers = []

    for u in numbers:
         if u % 2 == 0:
          even_numbers .append(u)
    return even_numbers
    
numbers = [8, 9, 6, 77, 45, 4, 7]
even_numbers = number_of_even_nmbers(numbers)
print(even_numbers)



   