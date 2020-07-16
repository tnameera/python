hrs = input("Enter Hours:")
h = float(hrs)
rate=input(" Enter rate")
r=float(rate)
if h < 40 :
    rpay=h*r
    print("pay per hr", rpay)
else :
    opay=(h-40)*1.5*r
    rpay=40*r
    tpay=opay+rpay
    print("pay per hr", tpay)
