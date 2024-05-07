# Get the absolute value of a number print(abs(-10))

x=abs(-10)
print(x)

##Convert an integer to a binary string print(bin(10))

x=bin(10)
print(x)

### Create a complex number print(complex(1, 2))

x=complex(1,2)

print(x)

##### Get the quotient and remainder of a division operation print(divmod(10, 3))

x=divmod(10,3)

print(x)

#####  Convert a number to a floating-point number print(float(10))

x=float(10)
print(x)

######  Convert a number to an integer print(int(10.5))
x=int(10.5)

print(x)

#######   Get the largest number in a sequence print(max(1, 2, 3))

x=max(1,2,3)

print(x)

#######  Get the smallest number in a sequence print(min(1, 2, 3))

x=min(1,2,3)

print(x)

####### Raise a number to a power print(pow(2, 3))

x=pow(2,3)

print(x)

######## Round a number to a specified number of decimal places print(round(10.5, 2))

x=round(9.123,10)#puchna hai
print(x)

#########

numlist=[19,21,46]
strlist=["one","two","three"]
setlist=['a1','b1','c1']
outputA=zip(numlist,strlist,setlist)

print(list(outputA))

########### chr() function

num=[77,101]
for i in num:
    print(chr(i))

####### enumerate()

name=['ani','nature','billo','sneha']
section=enumerate(name)
print(list(section))

##### float()

x=float(25)
print(x)

####### list()

list1=['ani','nature','vini','silent']
print('original list:',list1)
list1[1]='prakriti'
print("updated list:",list1)

####### Dict()

dic1={"falani":"jyoti arya",}
dic2={'name':'jyoti','education':'b.com','roll number':'258'}
dic3=dict(name='arya',age='21',roll='258')

print(dic1)



######### zip()

Name=['Ani','vini']
graduation=['B.A','B.Sc']
merge=zip(Name,graduation)

print(list(merge))

########## # use ord() function to find the Unicode of

x=ord('A')
y=ord('G')
z=ord('Z')
print(x,y,z)


########## Range()

for i in range(0,50,5):
    print(i)

######## set()

set=(set([1,2,2,5,8,9,7,8,6,8,9,2,1]))
print(set)


######### tuple()

x=('banana')
print(type(x))

######### len()

x=[1,2,2,5,8,9,7,8,6,8,9,2,1]
print(len(x))

######## str()

x=str('a')
y=str('b')

print(x,y)


########  Boolen function
a=bool(1)
b=bool(0)
c=bool(1)
d=bool(0)
e=bool(5)
# if(a==0 and b==0):
#         print("0")
# elif(a==0 and b==1):
#         print("0")
# elif(a==1 and b==0):
#         print("0")
# elif(a==1 and b==1):
#         print("1")
# else:
#         print("not applicable in boolen function")

   
# a=bool(1)
# b=bool(1)
# print(a&b)
print(a&((b&c)|d)|e)








