def bottles_of_beer():
    i = 99
    while i > 0:
        if i > 1:
            print(str(i) + " bottles of beer \n")
        else:
            print(str(i) + " bottle of beer")
        i -= 1

bottles_of_beer()
