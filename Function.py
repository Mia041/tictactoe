def name_function():
    '''
    Docstring: Information
    Input: no Input...
    output: Hello...
    '''
    print('Hello')

help(name_function)

def say_hello(name='NAME'):
    print('Hello'+ name)

say_hello()
result= say_hello('Jose')

def add(n1,n2):
    return n1+n2

result=add(20,30)
print(result)

#find out if the word "dog" is in a string?
def dog_check(mystring):
    return 'dog' in mystring.lower() #this is already a boolean
