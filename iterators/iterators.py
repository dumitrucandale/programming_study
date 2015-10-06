def fibo():
    a = 1
    b = 2
    while True:
        c = a + b
        a = b
        b = c
        yield c

a = fibo()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
