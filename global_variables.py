
x = 2

print(x, "\n---------------")

def foo():
    # Names listed in a global statement must not be defined as formal parameters
    #  or in a for loop control target, class definition, 
    #  function definition, import statement, or variable annotation.
    # Names listed in a global statement must not be used in the
    # same code block textually preceding that global statement.
    # f = x + 2 is an error
    global x
    # x: int also error
    x = 4
    print(x)
    x = 3
    print(x)


foo()
print(x)

# def foo(name,/, **kwds):
#     return 'name' in kwds

# print(foo(1, name= 2))



