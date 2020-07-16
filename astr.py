astr="Bob"
try:
    print("Hello")
    istr=int(astr)
    print("There")
except Exception as e:
    istr=-1
    print("Done", istr)
