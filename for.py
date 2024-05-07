# x=5
# n=6
# y=0
# for i in range(n+1):
#   y+=x+i
# print(y)

# x=5
# n=2
# y=0
# for i in range(n+1):
#   y+=x+i
#   print(y)


# #1+x/1+x*2/2+x*3/3+---------------x*n/n
#   x=5
#   n=2
#   fact=1
#   for i in range(1,n+1,2):
#       fact=fact*i
#       z=fact
#   print(z)
    
#   y=0
#   for i in range(n+1):
#    y+=(x**n/z)
#   print(y)

# ### FUNCTION KEY 
#   def herones(a,b,c):
#    s=(a+b+c)/2
#    return (s*(s-a)*(s-b)*(s-c))**(1/2)
#   x=herones(8,9,4)
#   print(x)

#   #####
#   def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
#   x=fact(5)
#   print(x).
def series(x,n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    z=fact
    y=0
    for i in range(n+1):
        y+=x**i/z
    return y
  
ans=series(4,6)  

print(ans)

#### 1+x**2/2+x**4/4+x**6/6-----------x**2*n/2*n

def seriesproblem(a,m):
    fact=1
    for i in range(1,m+1,2):
        fact=fact*i
    b=fact
    w=0
    for i in range(m+1):
        w+=a**2*i/2*i
    return w
ans=seriesproblem(4,6)
print(ans)

list1=['ani','nature','vini','sneha']
print=('original list',list1)
list1[1]="prakriti"
list1[-1]="silent"
print=("updated list",list1)

    
    
