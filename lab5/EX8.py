# punctul a)
def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b

def print_arguments(function):
    def new_f(*args,**kwargs):
        print(args,kwargs)
        return function(*args, **kwargs)
    return new_f

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)
print(x)
augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)
print(x)


#punctul b)
def multiply_output(function):
    def f(*args,**kwargs):
        return 2*function(*args,**kwargs)
    return f


def multiply_by_three(x):
    return x * 3


augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)
print(x)



#punctul c)
def augment_function(function,decorators):
    def f(*args,**kwargs):
        result = function
        for deco in decorators:
            result = deco(result)
        return result(*args, **kwargs)
    return f


decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
x=decorated_function(3,4)
print(x)
