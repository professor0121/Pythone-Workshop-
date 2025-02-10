 
#VARIABLES

##DEF:
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

if the 2 or more vriable having same data then the variable addresses are same

```python

#python  variables

a=100

print(a)

b=100.56

print(b)
c="hellow kaiz"

print(c)
d=100+30j

print(d)

r=100
print(r)

```
#valiables:
```python
#python comments 
'''
hello i am a comment
i am not excuted when program is running
'''
print("welcome to gyan sagar collage of engineering")
print("we are working on python programming")

print("statement 1")
print("statement 2")
print("statement 3" ,"\t", end ="")
print("statement 4")
print("statement 4")


```

#swapping:
```python
#wap to swap two numbers
#tradedional mathode for swapping

a=100
b=200

print("befor swap",a,b)

c=a
a=b
b=c

print('after swap ',a,b)

#new python advance mathod

a,b=100,200

print('before swapping the value of a and b respectively',a,b)

a,b=b,a

print('after swapping the value of a and b respectively',a,b)

```


#Data types using the types function or a method.another thing is that there is no character data type in python
```python
#Data type in pythons 

#Data type in pythons 

a=10
b=2+3j
c=2.4
d="hello abhishek"
e=True
f=[1,2,3,4]
g={'name':'abhi'}
h='a'

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
```


#tpye casting
```python
#Data type in pythons and the type casting of the data type in python

a=10
b=2+3j
c=2.4
d="hello abhishek"
e=True
f=[1,2,3,4]
g={'name':'abhi'}
h='a'

print(int(c))
print(str(c))
print(str(g))
 
print(complex(a))
```
#sum of 2 num usning the user input
```python
#wap to add 2 num taking the in put from the user

num1=int(input("enter the firstnum\t"))
num2=int(input("enter the firstnum\t"))

add=num1+num2

print('the sum is =\t\t',add)

```

#takinguserr input

```python

#wap to swap two nu taking input from user 

num1=int(input('enter first number\t'))
num2=int(input('enter second number\t'))
print('before swapping num1 and num2\t ',num1,num2)
num1,num2=num2,num1
print('after swapping num1 and num2 \t',num1,num2)
```


#show the greatest number
```python
#conditional statement

num1=int(input('enter first number\t'))
num2=int(input('enter second number\t'))

if num1>num2:
 print(num1,"is greater")

else:
 print(num2,'is greater')
```

#lader if  else
```python
#conditional statement using lader if else

num1=int(input('enter first number\t'))
num2=int(input('enter second number\t'))
num3=int(input('enter third number\t'))
num4=int(input('enter fourth number\t'))

if num1>num2 and num1>num3 and num1>num4:
 print(num1,"is greater")

elif num2>num1 and num2>num3 and num2>num4:
 print(num2,'is greater')

elif num3>num1 and num3>num1 and num3>num4:
 print(num3,'is greater')

else:
 print(num4,"is greater")
```
