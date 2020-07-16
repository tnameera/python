hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rates per Hours")
r=float(rate)
if h <= 40 :
    pay=(h*r)
    print ("Total pay is: ",pay)
else:
    pay = (40)*r
    opay = (h-40)*1.5*r
    tpay = pay+opay
    print("Total pay is:",tpay)
