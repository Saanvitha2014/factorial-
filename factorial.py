def factorial(x):
    '''this is a recurse function to find the factorial of an integer'''

    if x==0 or x==1:
        return 1 
    else:

        return x*factorial(x-1)
    print(factorial._doc_)
    print("factorail of 0:",factorial(0))
    print("factorail of 1:",factorial(1))
    print("factorail of 2:",factorial(2))
    print("factorail of 5:",factorial(5))
    print("factorail of 10:",factorial(10))
