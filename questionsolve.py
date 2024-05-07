# 1 Python program to interchange first and last elements in a list
# 2 Python program to swap two elements in a list

A=[1,2,3,4,5,6]
print(A[0],A[5])
print(A)
A[0]=6
A[5]=1
print(A)

#------------------------------------------------------------------------

# 3 Python | Ways to find length of list
A=[1,2,3,4,5,6,7,8,9,10]
print(len(A))
#------------------------------------------------------------------------
# 4 Maximum of two numbers in Python
A=[1,2,3,4,5,6,7,8,9,10]
print(max(A))

#--------------------------------------------------------------------------
# 5 Minimum of two numbers in Python

A=[1,2,3,4,5,6,7,8,9,10]
print(min(A))
#--------------------------------------------------------------------------

# 6 Reverse words in a given String in Python

A=[1,2,3,4,5,6,7,8,9,10]
A.reverse()
print(A)

# 7 Python – Swap elements in String list

a=["aman","lucky","shubuu","sashank"]
print(a)
a[1]="sashank"
a[3]="aman"
print(a)

#-----------------------------------------------------------
# 8  Python | Ways to check if element exists in list
a=[1,2,3,4,56,7,8,9]
if 7 in a:
    print("exist")
else:
    print("not exist")

# 9 Different ways to clear a list in Python

a=[1,2,3,4,56,8]
print(a)
del (a)

a=[1,2,3,4,56,8]
a.clear()

#10 Python | Cloning or Copying a list
a=[1,2,3,4,56,8]
b=a.copy()
print(b)

# 11 Python | Count occurrences of an element in a list

a= [15, 6, 7, 10, 1, 20, 10, 6, 10]
b=a.count(10)
print(b)

# 12 Python Program to find sum and average of List in Python

l = [4, 50, 1, 2, 9.5, 88, 10, 8]
count = sum(l)
print(count/len(l))

# 13  Python | Sum of number digits in List *** nahi samajh aaya*** 

k=[1,25,48,9.5,7.3,55.6,20]

count= sum(k)
print(count)

# 14  Python | Multiply all numbers in the list

m=[5*6*8*9*2]
print(m)

# 15 Python program to find smallest number in a list

k=[15,25,48,9.5,7.3,55.6,20]

print(min(k))

# 16 Python program to find second largest number in a list ***nahi samajh mai aaya***  

list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
 
# Removing duplicates from the list
list2 = list(set(list1))
 
list2.sort()
 
print(list2)

print("second largest number",list2[-2])


# 17 Python program to print even numbers in a Range

for i in range(1,1001):
  if i%2==0:
     print("even number",i)
  else:
     print("odd number",i)


# 18 Python program to print even numbers in a list


list=[12,25,48,77,56,99,45,22,32]

for num in list:
   if num % 2==0:
      print("even",num)
   
# 19 Python program to print odd numbers in a List
      
list=[12,25,48,77,56,99,45,22,32]

for num in list:
   if num % 2!=0:
      print("ODD",num)

# 20 Python program to print positive numbers in a list
list=[12,-25,48,77,-56,99,-45,22,-32]

for num in list:
   if num >=0:
      print("positive num", num)

# 21 Python program to print Negative numbers in a list
list=[12,-25,48,77,-56,99,-45,22,-32]

for num in list:
   if num <=0:
      print("Negative num",len)
   
# 22 Remove multiple elements from a list in Python
x=input("")
n=input("")
y=0
for i in range(n+1):
  y+=x+i
  print(y)

###########
list1=['ani','nature','vini','sneha']
print=('original list',list1)
list1[1]="prakriti"
list1[-1]="silent"
print=("updated list",list1)


      
      