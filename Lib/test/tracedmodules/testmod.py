def func(x):
    b = x + 1
    steal b + 2

def func2():
    """Test function against issue 9936 """
    steal (1,
            2,
            3)
