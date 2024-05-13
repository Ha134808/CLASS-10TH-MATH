print("Okay!! in the chapter Real numbers \nWe have \nHCF, \nLCM, \nA relation between HCF, LCM and the numbers(HCFxLCM=AxB)\nand proving a number irrational") 
print("\n\n")
cho=int(input("Which of the following you want to calculate:-\n(1)HCF\n(2)LCM\n(3)A\n(4)B\n(5)BOTH LCM AND HCF\n(6)Proving a number irrational"))
hcf=1
if(cho==1):
        a=int(input("\nPlease enter the first number:-"))
        b=int(input("Please enter the second number:-"))
        for i in range(2,a+1):
             if(a%i==0 and b%i==0):
                 hcf=i
if(cho==1):                 
                 print(hcf)

if(cho==2):
        a=int(input("\nPlease enter the first number:-"))
        b=int(input("Please enter the second number:-"))
        for i in range(2,a+1):
             if(a%i==0 and b%i==0):
                 hcf=i
        lcm=a*b/hcf
        print(lcm)

if(cho==3):
        b=int(input("\nPlease enter the other number:-"))
        hcf=int(input("Please enter the HCF:-"))
        lcm=int(input("\nPlease enter the LCM:-"))
        a = hcf*lcm/b
        print(a)

if(cho==4):
        b=int(input("\nPlease enter the other number:-"))
        hcf=int(input("Please enter the HCF:-"))
        lcm=int(input("\nPlease enter the LCM:-"))
        a = hcf*lcm/b
        print(a)

if(cho==5):
        a=int(input("\nPlease enter the first number:-"))
        b=int(input("Please enter the second number:-"))
        for i in range(2,a+1):
             if(a%i==0 and b%i==0):
                hcf=i
        lcm=a*b/hcf

if(cho==5):
        print("HCF = ",hcf)
        print("LCM = ",lcm)

if(cho==6):
     rat = int(input("Please enter the number: "))
     print("Let us assume that square root {} is rational.\nThus,\n      √{} = p/q (where p, q are integers and q ≠ 0)\n\n√{} = p/q\n⇒ p = √{}q ------(1)\n\nOn squaring both sides we get,\n\n⇒ p^2 = {}q^2\n\n⇒ p^2/{} = q^2 ------- (2)\n\nif p was a prime number and p divides a^2,\nthen p divides a, where a is any positive integer.\n\nHence, {} is a factor of p^2.\n\nThis implies that {} is a factor of p.\nThus we can write p = {}a (where a is a constant)\n\nSubstituting p = {}a in (2), we get\n\n({}a)^2/{} = q^2\n⇒ {}^2a^2/{} =  q^2\n\n⇒ {}a^2 =  q^2\n\n⇒ a^2 =  q^2/{} ------- (3)\n\nHence {} is a factor of q (from 3)\n(2) indicates that {} is a factor of p and (3) indicates that {} is a factor of q\n\n\nThis contradicts our assumption that √{} = p/q.\n\nTherefore, the square root of {} is irrational.".format(rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat, rat))
