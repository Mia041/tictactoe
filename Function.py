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



def pig_latin(word):
    if word[0] in 'aeiou':
        return word +'ay'
    else:
        return word[1:]+ word[0] +'ay'

result=pig_latin('word')
print(result)

def myfunc(a,b,c=0,d=0): #by default
    #returns 5% of the sum of a and b
    return sum((a,b))*0.05 #pass in a tuple

def myfunc(*args): *anything
    return sum(args)*0.05 #user can pass in as many as they want and is treated as tuples




def myfun(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {}{}'.format(args[0],kwargs['food']))

def myfunc(*args):
    return sum(args)

num=myfunc(1000,20394,4,58)
print(num)




st='Anthropomorphism'
ss=[]
def even_odd(st):
    for index, i in enumerate(st):
        if index%2==0:
            ss.append(i.lower())
        else:
            ss.append(i.upper())
    return ''.join(ss)
print(even_odd(st))




result=[]
def myfunc(string):
    for i in range(len(string)):
        if i==3 or i==0:
            result.append(string[i].upper())
        else:
            result.append(string[i].lower())
    return ''.join(result)

print(myfunc("macdonald's"))


def myfunc_1(sentence):
    words=sentence.split()
    words.reverse()
    reversed_sentence = ' '.join(words)
    return reversed_sentence
print(myfunc_1('how are you today'))


#def myfunc_2(*args):
#    for i in range(0,len(args)):
#        if num[i] is 0:
#            pass


#print(myfunc_2(1,2,3,4,5,6,0,0,7))


def myfunc_3(num):
    if num < 2:
        return 0
    ss=0
    for t in range(2, num+1):
        for x in range(2,t-1):
            if t%x==0:
                break
        else:
            ss+=1
    return ss
print(myfunc_3(100))
