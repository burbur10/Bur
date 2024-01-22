#v= -8
#assert (v==0),'v is positive'
try:
    d=5/7
    e=d +7
except ZeroDivisionError as e:#print("")
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('excellence')
#CREATING OUR OWN EXCEPTONS
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message =message
        self.value =value

def text_value(c):
    if c>100:
        raise ValueTooHighError('VALUE IS TOO HIGH')
    if c<5:
        raise ValueTooSmallError('value is too small', c) 
try:
    text_value(3)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)