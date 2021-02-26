def fab(n):
    if n < 0:
        print("Invalid Number")
    elif n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fab(n-1) + fab(n-2)
    
print(fab(5))
print(fab(9))
