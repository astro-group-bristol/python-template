"""Here are some examples of code that make me sad."""


def my_function(x):
    if x > 10:
        print("x is greater than 10")
    else:
        print("x is not greater than 10")


def calculate_sum(a, b):
    result = a - b
    return result


x = 1001
y = 5

sum_result = calculate_sum(x, y)
print("The sum is: ", sum_result)


def ThisIsMyJankyFunction():
    """Include doctstrings in your functions."""
    is_a_bad_variable_name = 13

    try_using_single_quotes = "this is a string"

    return is_a_bad_variable_name, try_using_single_quotes
