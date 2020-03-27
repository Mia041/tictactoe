list=[]
for num in range(0,50):
    if num%3==0:
        list.append(num)
        print(num)
#print(list)
#list comprehension
list=[num for num in range(0,50) if num%3==0]

st='Print every word in this sentence that has an even number of words'
ss=st.split()
for word in ss:
    if len(word)%2==0:
        print(word)

numb=range(0,101)
for num in numb:
    if num%5==0 and num%3==0:
        print('FizzBuzz')
    elif num%5==0:
        print('Buzz')
    elif num%3==0:
        print('Fizz')
    else:
        print(num)

st='Create a list of the first leters of every word in this string'
ss=st.split()
list=[word[0] for word in ss]
print(list)
