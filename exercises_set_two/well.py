#def count(lst):

  #  even = 0
  #  odd = 0

   # for i in lst:
   #     if i % 2 == 0:
   #        even += 1
    #    else:
     #       odd += 1

    #return even, odd
#lst = (12, 13, 8, 5, 48,1, 6, 10)
#even, odd = count(lst)
#print("even numbers:", even)
##print("odd numbers:", odd)

#fibonacci
def fib(n):
    a = 0
    b = 1

    if n == 1:
       print(a)
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a+b
            a = b
            b = c
            print(c)
fib(20)