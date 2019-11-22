# Data structures practice 0
# Author: ___________

def mean(values):
    """
    Returns the mean (average) of the values. 
        >>> mean([1, 3, 5])
        3
        >>> mean(range(100))
        49.5
    """
    return 0

def span(values):
    """
    Returns the distance between the largest and the smallest value 
    in `values`.
        >>> span([40, 30, 20, 10])
        30
        >>> span(range(100))
        99
    """
    return 0

def get_stats(values):
    """ 
    Returns a dict of statistics describing `values`.
        >>> stats([1, 2, 2, 7])
        {
            "max": 7, 
            "min": 1, 
            "len": 4,
            "mean": 3, 
        }
    """
    return {
        "max": 0,
        "min": 0,
        "len": 0,
        "span": 0,
        "mean": 0,
    }

def count_value(values, target):
    """
    Counts how many times `target` appears in `values` and returns an int.
        >>> values = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4] 
        >>> count_value(values, 2)
        3
        >>> count_value(values, 3)
        2
        >>> count_value([], 3)
        0
    """
    return 0
