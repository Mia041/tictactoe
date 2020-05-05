#data type: integer, floating
name='Sam'
last_letters=name[1:]
print(last_letters)
x='hello world'
x=x + " it is beautiful outside"
print (x)
print (x.upper())
print (x.split())

#strings,format
print ('This is a string {}'.format('inserted'))
print('the {} {} {}'.format('fox','brown','quick'))
print('The {f} {f} {f}'.format(f='fox',b='brown',q='quick'))
result=100/777
print("The result is {r:1.3f}".format(r=result))
name = "Jose"
print(f'Hello, his name is {name}')
name = 'Sam'
age ='3'
print(f'{name} is {age} years old')
p="Pyton rules"
print("we're learning {}".format(p))

#list can be indexed and sliced just like strings
#brackets, separated by commas
#functions = new_list.append('') to add to the end
#new_list.pop() to pop ou whatever you want, space means at the end, 0 is the first
new_list=['a','e','b','x']
num_list=[1,4,5,7,3]
print(num_list)

#dictionary defined by curly brackets{} notations, lists in []
prices_lookup={'apple':2.99,'oranges':1.99,'milk':5.}
prices_lookup['apple']
d={'k1':123,'k2':[0,1,2],'k3':{'kurney':100}}
print(d['k3']['kurney'])
print(d.keys)
print(d.values)

#similar to list, tuple is defined by parentesis(),differet is it's immutability
mylist=(1,2,3)
t=('one',2)
t[0]
t[-1]
t=('a','a','b')
print(t.count('a'))
print(t.index('b'))

#unique set of elements, curly brackets{},if you add same, won't repeat
myset=set()
myset.add(1)
myset.add(2)
myliset=[1,1,1,1,1,1,12,2,2,2,3,3,3]
print(set(mylist))
Mississippi='Mississippi'
print(set(Mississippi))

#Booleans True or False statements
type(False)
1>2
1==1
b=None
