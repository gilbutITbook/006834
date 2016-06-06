a = ['a', 'b', 'c']

number = int(raw_input('input a number >'))

try:
    b = a[number]
except IndexError:
    print 'Error!'
else:
    print b
finally:
    print 'end of program'
