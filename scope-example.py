def outer_function():
    b = 20              #local namespace of outer function
    def inner_func():
        c = 30          #nested local namespace of inner function

a = 10                  #global namespace
#Here, the variable a is in the global namespace. Variable b is in the local
#namespace of outer_function() and c is in the nested local namespace of inner_function().

#When we are in inner_function(), c is local to us, b is nonlocal and a is global.
#We can read as well as assign new values to c but can only read b and a from inner_function().
