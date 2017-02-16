# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)

def roots(a, b, c):
        try:
            r =(b ** 2)- (4 * a * c)
            import cmath
            sq = cmath.sqrt

            if r == 0:
                x = (-b) / (2 * a)
                y = (-b) / (2 * a)
                print('the roots are :', x, ',', y)

            elif r >  0:
                x = ((-b) + sq(r)) / (2 * a)
                y = ((-b) - sq(r)) / (2 * a)
                print('the roots are :', x, ',', y)

            if r < -1:
                i = sq(-1)
                x = (-b + (sq(r * (i ** 2)))) / (2 * a)
                y = (-b - (sq(r * (i ** 2)))) / (2 * a)
                print( 'the roots are :', x, ',', y)
        except:
            print
            'wrong inputs , please enter numbers only'
        pass

def integrate(function, lower, upper):
    x = lower
    sum = 0
    while x <= upper:
        sum += eval(function) * 0.01
        x += 0.01
    return(sum)
if __name__ == '__main__':
    print(fact(5))
    print(roots(3, 2, 1))
    print(integrate('x ** 2 - 1', -1, 1))