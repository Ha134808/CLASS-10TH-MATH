print(" Okay!! in the chapter Polynomials\n We have\n The basic structure of a Quadratic Polynomial(ax^2+bx+c)\n About how to find the zeroes of polynomial\n a relation between the zeroes[α,β] of polynomial and cofficients as [α+β=-b/a & α*β=c/a]\n And a formula to derive the quadratic polynomial using zeroes of it as [x^2-(a+b)x+(a*b)]\n\n")
cho1 = int(input("Which of the following you want to calculate from the following:-\n (1)Zeroes of polynomials\n (2)Find cofficient of x^2 (a)\n (3)Find cofficient of x (b)\n (4)Find constant (c)\n (5)Derive a quadratic polynomial from its zeroes"))
if(cho1==1):
    a = int(input("Please enter the cofficient of x^2 [a]--"))
    b = int(input("Please enter the cofficient of x [b]--"))
    c = int(input("Please enter the constant [c]--"))
    cof=[a,b,c]
    roots = numpy.roots(cof)
    print(roots)

if(cho1==2):
    aorb = int(input("by which methord you want to calculate:-\n(1)Using α+β= -b/a\n(2)Using α.β= c/a"))
    if(aorb==1):
        b = int(input("Please enter the cofficient of x [b]--"))
        α= int(input("Please enter α [First zero of polynomial]--"))
        β= int(input("Please enter β [Second zero of polynomial]--"))
        b1= b* -1
        x2 = b1/(α+β)
        print("Value of a is ",x2)


    if(aorb==2):
       c = int(input("Please enter the constant [c]--"))
       α= int(input("Please enter α [First zero of polynomial]--"))
       β= int(input("Please enter β [Second zero of polynomial]--"))

       x2 = c/(α*β)
       print("Value of a is ",x2)
                                                                                               

if(cho1==3):
    a = int(input("Please enter the cofficient of x^2 [a]--"))
    α= int(input("Please enter α [First zero of polynomial]--"))
    β= int(input("Please enter β [Second zero of polynomial]--"))
    b=(α+β)*a
    b1= b* -1
    print("Value of b is ",b1)

if(cho1==4):
    a = int(input("Please enter the cofficient of x^2 [a]--"))
    α= int(input("Please enter α [First zero of polynomial]--"))
    β= int(input("Please enter β [Second zero of polynomial]--"))
    c=(α*β)*a
    print("Value of c is ",c)

if(cho1==5):
    α= int(input("Please enter α [First zero of polynomial]--"))
    β= int(input("Please enter β [Second zero of polynomial]--"))
    b=(α+β) * -1
    ##b1=str(b)
    c=(β*α)
    ##c1=str(c)
    print("The quadratic polynomial is -- x^2 - ({}x) + {}".format(b,c)) 

    
