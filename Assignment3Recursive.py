def T(x):
    '''Recursive Definition'''
    if x == 1:
        return 2

    elif x > 1:
        return (T(x-1))+(x*x)+x



def R(x):
    '''Closed Form Solution'''
    return 2 + ((((2*x*x*x)+(3*x*x)+(x))/6)-1)+((((x*x)+x)/2)-1)



def main():
    strline = "{0:<3} | {1:<6} | {2:<6}\n"
    for i in range(1, 41):
        print(strline.format(i, T(i), R(i)))


main()