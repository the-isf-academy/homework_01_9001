# HW 1.90001 Lists Practice
# Author: ___________

def mean(values):
    """
    Returns the mean (average) of a list of values.
    
    input: list of ints/floats
    output: int/float
    
        >>> mean([1, 3, 5])
        3
        >>> mean(range(100))
        49.5
    Hint: you've done this problem before in HW 1.2...Feel free to adapt your code.
    """
    return 0

def create_ones_list(length):
    """
    Creates a list that has `length` number of elements, and each element is the integer 1.
    Returns the list.
    
    input: int
    output list of ints
    
        >>> create_ones_list(4)
        [1,1,1,1]
        >>> create_ones_list(15)
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        >>> create_ones_list(0)
        []
    """
    return 0

def is_even(values):
    """
    Returns True if the length of the list is even. Returns False otherwise.

    input: list of any type (values)
    output: boolean

        >>> is_even(["a", "b", "c"])    def test_count_value_1(self):
        self.assertEqual(test_count_value_1([1, 1, 1, 1, 2, 2, 2, 3, 3, 4], 2), 3)
        self.assertEqual(test_count_value_1([1, 1, 1, 1, 2, 2, 2, 3, 3, 4], 3), 2)
        self.assertEqual(test_count_value_1([], 1), 0)
        False
        >>> is_even([1,1,1,2,4,5])
        True

    By the way, you'll use this for box and whisker plot lab.
    """
    return False

def make_even(string_list):
    """
    If the list is even, return string_list without changing anything.
    If the list is not even, append the string "SIKE" to the end of string_list, then return the string_list.

    input: list of strings (string_list)
    output: list of strings (string_list)

    >>> make_even(["monday", "tuesday", "wednesday"])
    ["monday", "tuesday", "wednesday", "SIKE"]

    >>> make_even(["7", "8", "9", "10"])
    ["7", "8", "9", "10"]

    Hint: you can use is_even() inside this function ...
    """
    return 0

def count_value_1(values, target):
    """
    Counts how many times `target` appears in `values` and returns an int.
    
    input: a list of any type (values) and an int/float (target)
    output: an int
    
        >>> values = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        >>> count_value(values, 2)
        3
        >>> count_value(values, 3)
        2
        >>> count_value([], 3)
        0
    """
    return 0

def count_value_2(values, target):
    """
    You wrote the function above using one type of for-loop.
    Now write the exact same function as above, except use the other type of for-loop.
    
    input: a list of any type (values) and an int/float (target)
    output: an int

    Hint: What are the two types of for-loops, you ask? Check out the Unit 0 Loops Lab.
    Or, here's a hint:
    1. for _ in range(___):
    2. for _ in ___:
    """
    return 0
