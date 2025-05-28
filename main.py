#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. 2nd_name is not valid because it starts with a number, it must start with a letter or underscore.
3. age is a valid name because there it is just a word but also it isn't predefined by python
4. total_amount is perfectly valid as well because it is using snake case.
5. while is not valid because it is predefined in python. Its specifically used for while loops, so it cannot be a valid variable name.
6. Student is also valid as well because it is just a word, however, we don't typically capitalize variables.
7. my-variable is not valid because it has a dash between the words which will return an error in python.
8. for, like while, has a predefined function in python dedicated to running for loops, so it is not a valid variable name.
9. _temp is valid because it uses snake case.
10. value# is not a valid name because #s are special characters.
Your solution goes here


"""
# Problem 2
"""
1. calculate_total is a valid function name because it is written in snakecase.
2. 3rd_function is invalid as a function name because it starts with a number.
3.print_values is a valid function name because it is in snakecase.
4. find-item is invlaid because it contains "-" which is a special character.
5. def is invalid as a function name because it is a reserved word in python.
6. updateProfile is a valid function name because it is just letters.
7. my_function is a valid function name because it is in snake case.
8. try is a valid function name because it is not a reserved word.
9. init_data is a valid function name because it is in snake case.
10. value@function is an invalid function name because "@" is a special character. 


"""
# Problem 3
"""
1. Valid, returns false because A(true) and B(false) gives A and B (false).
2. Valid, returns true because A is true and B is comparing the length of the two strings and is also true.
3. Valid, returns false because the statement is true but the not negates the true to a false.
4. Not valid, because to compare in python you need "==" instead of just one "=".
5. Not valid, because 5 does not return a true or false.
6. Valid, returns false because the first one is true and the second one is false.
7. Valid, this should return true because it is true that false is equal to false.
8. Valid, this will return true because the statement is true. 
9. Valid, this will return true because the expression evaluates to true or true which is true.
10. Not valid, 5 and 4 don't return true or false.


"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
