
#def person(name, **data):

#    print(name)
#    print(data)

#person('brian', age = 45, city = 'tongaren', mobile = 986532)
def count(lst):

    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
           even += 1
        else:
            odd += 1

    return even, odd
lst = (12, 13, 8, 5, 48,1, 6, 10)
even, odd = count(lst)
print(even)
print(odd)