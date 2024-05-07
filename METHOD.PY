#Change of item values 

a=[1,2,3,4,5,6,7,8,9,10]
print(a)
a[2]="aman"
print(a)

#swapping two values 
a,b=10,20

print(a)
print(b)

a,b=b,a

print(a)
print(b)

#using changeble or index value to change the variable value it also a swapping

a=[2,3,4]
print(a[0],a[1],a[2])
a[0]=4
a[2]=2
print(a[0],a[2])

# -------------------------------M-E-T-H-O-D-S--------------------------------------------------

#-----INSERT METHOD ------------------

a=[1,2,3,4,5,6,7,8,9]
a.insert(2,"A")
print(a)

#---------Append method---------------to add the element in last place(n-1)index
a=[1,2,3,4,5,6,7,8,9]
a.append(10)
print(a)

#--------Extend Method----------

a=[1,2,3,4,5,6,7,8,9]
print(a)
b=[10,11,12,13,14,15]
a.extend(b)
print(a)

#----Remove method-----------

a=[1,2,3,4,5,6,7,8,9]
a.remove(3)
print(a)

#-------Del method---------

a=[1,2,3,4,5,6,7,8,9]
del a [3]

#--------Clear method---------
a=[1,2,3,4,5,6,7,8,9]
a.clear()
print(a)

#--------sort Method----------

a=[58,67,25,64,89,22]
a.sort()
print(a)

#-------reverse Method---------
a=[58,67,25,64,89,22]
a.reverse()
print(a)

#--------COPY METHOD------------
a=[1,2,3,4,5,6,7,8,9]

b=a.copy()
print(b)

#---------join method -----------

a=[2,3,4,5,6,7,8]
b=[2,3,4,5,6,7,8]
c=a+b
print(c)


#---------Index method------------

fruits =[23,78,2,6,4,825,5,5]
 
y=fruits.index(825)

print(y)


#----------Pop Method----------

fruits =[23,78,2,6,4,825,5,5]
fruits.pop(5)
print(fruits)

#----------maximum method-----------

a=[23,78,2,6,4,825,5,5]
print(max(a))

#-----------minimum method----------

a=[23,78,2,6,4,825,5,5]
print(min(a))


#-----------------------------End--------------------------------------------------------#


                      #---------------T-U-P-L-E -----------------------#
#---------ACCESS TUPLE-----------


a=(1,2,3,4,5,6,7,8,9)
print(a[2])

#-----------------------------

tuple=("apple","banana","orange","grapes")
print(tuple[-2])

#-----------------------------
tuple=("apple","banana","orange","grapes","kiwi")
print(tuple[0:4])

tuple=("apple","banana","orange","grapes")
print(tuple[:3])

tuple=("apple","banana","orange","grapes","mango","kiwi")
print(tuple[0:])

#------------------------UPDATE-TUPLE----------------------------


#---------CHANGE TUPLE--------------





a=[1,2,3,4,5,6]
x=0
y=0
for num in a:
    if num%2==0:
         x=x+1
         print(x)
    else:
        y=y+1
        print(y)
print(x,y)

list=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,101):
    if i%2==0:
        print(i)
    elif i%2!=0:
        print(i)

#-------------- tuple----------------
        

set1={"a","b","c","d"}
set2={1,2,3}
set1.update(set2)
print(set1)

y=input("enter a letter")

if (y=='a' or y=='e' or y=='i' or y=='o' or y=='u'):

 print("vowel" )

else:
    
 print("consonent")

n=input("enter a number")

if(n % 2 == 0):
   print ("even number")
else:
   print("odd number")   



