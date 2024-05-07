n=int(input("enter the principal amount"))


if(n>10000) and (n<100000):
    time=float(input("time--"))
    rate=5.5
    simple_intrest=(n*time*rate)/100
    print("S.I",simple_intrest)
    payble_amount=simple_intrest+n
    print("the total payment is",payble_amount)
    months_1=payble_amount/(time*12)
    accurate_payble=12*months_1
    print("1 year amount payble by user",accurate_payble)

elif(n>100000) and (n<10000000):
     time=float(input("time--"))
     rate=7.5
     simple_intrest=(n*time*rate)/100
     print("S.I",simple_intrest)
     payble_amount=simple_intrest+n
     print("the total payment is",payble_amount)
     year_1=payble_amount/(time*12)
     accurate_payble=12*year_1
     print("1 year amount payble by user",accurate_payble)
