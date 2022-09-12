def safe_print_list_integers(my_list=[], x=0):
    try:
        n = 0
        for i in range(x):
            if type(my_list[i]) == int:
                n += 1
                print("{:d}".format(my_list[i], end=" "))
    except TypeError:
        pass
    finally:
        if n < x:
            print('')
            return n
        else:
            print('')
            return x
