a = 1
b = 1
print(globals())
print(locals())


def foo():
    b = 2
    global a
    a = 2
    print(globals())
    print(locals())
    print(a, b)


foo()
