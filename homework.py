a={1,2,3,4,5,6}
b={"a","b","c","d","e"}
c={True,False}
d={1,2,"a","c","d",True}
e={True,"c",1,2,"b",False}


a.union(b)

def herones(a,b,c):
   s=(a+b+c)/2
   return (s*(s-a)*(s-b)*(s-c))**(1/2)
x=herones(8,9,4)
print(x)