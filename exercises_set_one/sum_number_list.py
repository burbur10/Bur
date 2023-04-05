def numbers(num):
    total = 0
    for number in num:
        total+=number
    return total
addition = [int(input("input the first number")), int(input("input the second number")), int(input("input the third number"))]
sum_total = numbers(addition)
print(sum_total)