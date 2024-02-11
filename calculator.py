print("Calculator")
print("Enter 1 for '+'")
print("Enter 2 sir'-'")
print("Enter 3 for '*'")
print("Enter 4 for'/'")
while True:
    a=int(input("Enter 1st numeric value:"))
    b=int(input("Enter 2nd numeric value:"))
    c=int(input("Enter operator to be used:"))
    if(c==1):
        d=a+b
        print('sum is:',d)
    elif(c==2):
        e=a-b
        print('difference is:',e)
    elif(c==3):
        f=a*b
        print('product is:',f)
    elif(c==4):
        g=a/b
        print('division is:',g)
    else:
        print('wrong choice')
    h=input('do you want to continue?(y/n)')
    if(h=='n'):
        print('leaving loop...........')
        break
