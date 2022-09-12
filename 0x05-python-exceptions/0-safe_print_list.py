def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for i in my_list:
            n += 1
        for i in range(x):
            print(my_list[i], end="")
    except IndexError:
        pass
