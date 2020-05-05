x = open('test.txt',"r")
#x.write('\nToday is Tuesday')
x.close()
#'w','r'

#Booleans
r=(2==2)
print(r)
2==1
'hello'=='bye'
3!=3 #not equal to
4!=5
2>1
1<2
2<=2
4<=1
not 1==1 and 2==4
1==1 or 2==5

#condition indent is important
if condition:
    pass
elif condition:
    sth
else:

loc='Bank'
if loc=='Auto Shop':
    print('Cars are cool!')
elif loc=='Bank':
    print('Money is cool!')
elif loc==('store'):
    print('Welcome!')
else:
    print('I do not know much')

#forloops:iterable:going through sth, list,dictionary,strings
mylist=[1,2,3,4,5,6,7,8,9,10]
for num in my_list:
    print(ioio)

list_sum=0

for num in mylist:
    list_sum=list_sum + num
    print(list_sum)

for letter in 'Hello World'
    print('cool')

mylist= [(1,2),(3,4),(5,6)]
for a,b in mylist,
    print(a)
    print(b)

#iterate through dictionary
d={'k1':1,'k2':2,'k3':3}
for key,value in d.items():
    print(value)
