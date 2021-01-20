#if we declare a as global, all the reference and assignment go to the global a.
'''
Similarly, if we want to rebind the variable b, it must be declared as nonlocal.
The following example will further clarify this.'''


def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)

a = 10
outer_function()
print('a =',a)

#Here, all reference and assignment are to the global a due to the use of keyword global.
def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)

a = 10
outer_function()
print('a =',a)
