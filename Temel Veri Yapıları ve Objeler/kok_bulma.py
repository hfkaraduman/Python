#ikinci derereceden denklemin koklerini bulma

#Denklem ax^2+bx+c seklinde bir denklem olsun

a=int(raw_input("a:"))
b=int(raw_input("b:"))
c=int(raw_input("c:"))

delta=b**2-4*a*c

k1=(-b-delta**0.5)/2*a
k2=(-b+delta**0.5)/2*a

print("Birinci kok:{}\nIkinci kok:{}".format(k1,k2))

