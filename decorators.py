#code1
# A simple decorator function
def decorator(func):
  
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator

def greet():
    print("Hello, World!")

greet()

# code 2
'''
def decfun(func):
    def inner():
        print('hai satish')
        func()
        print('how are you')
    return inner
@decfun
def start():
    print('good mrng')
start()    '''


#code3
'''
def decfun(func):
    def inner(a,b):
        if b==0:
            print("b must not be zero")
        else:
            return func(a,b)
    return inner    
@decfun            

def div(a,b):
    return a/b
print(div(2,1))
print(div(2,0)) 

'''