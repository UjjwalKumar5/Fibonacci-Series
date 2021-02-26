import math

pow(3,2)
for i in range(1,11):
    print(pow(i,2))    # for print the square of first 10 numbers
    print(pow(i,3))    # for print the cube of first 10 numbers
    print(pow(i,0.5))  # for print the square root of first 10 numbers
    
lst = [11,32,34,54,67,87,24,55,36,87]
max(lst)               # returns the maximum numbers
min(lst)               # returns the minimum numbers
math.ceil(5)           # ceil and floor numbers
math.copysign(5,-1)    # copy the sign of y
math.factorial(5)      # returns the factorial of the numbers
math.fmod(40,6)        # returns the remainder
math.frexp(5)          # returns the exponent of x as the pair of (m,e)
math.sum(lst)          # returns the sum of the values present 
math.exp(5)            # returns the exponent of (e,5)
math.expm1(6)          # returns the value of e**x-1
math.sqrt(5)           # returns the square root of x
math.gcd(46,84)        # returns the greatest common divisor
math.lcm(25,20)        # returns the least common multiple
math.nextafter(34,36)  # returns the next number in floting point either towards zero/opposite
math.prod(lst)         # returns the product of all availale iterables
math.remainder(6,5)    # returns the reaminder
