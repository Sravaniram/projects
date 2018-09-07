def add(x,y):
    return(x+y)
def mul(x,y):
    return(x*y)
def sub(x,y):
    return(x-y)
def div(x,y):
    return(x/y)
x=float(input())
choice=str(input())
y=float(input())
if choice=='+':
    print(add(x,y))
elif(choice=='-'):
    print(sub(x,y))
elif(choice=='*'):
    print(mul(x,y))
elif(choice=='/'):
    print(div(x,y))
