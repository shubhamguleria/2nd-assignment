#Question1
'''
#ZeroDivisionError: division by zero
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("Handled the Error")
'''
#Question2
'''
#It is an Index Error.
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("This is the exception of Indexerror")
'''
#Question3
'''
An exception
Traceback (most recent call last):
  File "/Users/katoch/Desktop/3.py", line 2, in <module>
    raise NameError("Hi there")
NameError: Hi there
'''
#Question4
'''
-5.0
a/b result in 0
'''

#Question5
#Import_Error
'''
try:
  from .local_settings import *
except ImportError:
  print("this is the import error")
'''
#Value_Error
'''
def read(a):
    

    try:
        b=int(input("enter the value: "))
    except ValueError:
        print("this is the exception of value error")
'''
#Index_Error
'''
def read(a):
    try:
        print(a[25])
    except IndexError:
        print("this is the exception of Indexerror")
read(a=[1,2,3,4,5,67,2,6,7,6,4])
'''
#Question6
'''
def AgeTooSmallError(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 18:
            print("Sorry, you entered an inappropriate age.")
            continue
        else:
            print("You entered an appropriate age")
            break
    return value

age = AgeTooSmallError("Please enter your age: ")

'''
