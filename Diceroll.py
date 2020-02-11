import random

someInt = float(input("How many rolls? "))
print(str(someInt)+ " rolls")



roll = random.randint(1,6)



i = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
while(i<someInt):
    roll = random.randint(1,6)
    if(roll == 1):
        a= a+1
    if(roll == 2):
        b = b+1
    if(roll == 3):
        c = c+1
    if(roll == 4):
        d= d+1
    if(roll == 5):
        e = e+1
    if(roll == 6):
        f = f+1

  
    i += 1
    r = (a/i)*100
    z = (b/i)*100
    x = (c/i)*100
    t = (d/i)*100
    q = (e/i)*100
    m = (f/i)*100

print("1: " + str(a) +"/" +str(i)+ "= "+ str(r)+ "%" )
print("2: " + str(b) +"/" +str(i)+ "= "+ str(z)+ "%" )
print("3: " + str(c) +"/" +str(i)+ "= "+ str(x)+ "%" )
print("4: " + str(d) +"/" +str(i)+ "= "+ str(t)+ "%" )
print("5: " + str(e) +"/" +str(i)+ "= "+ str(q)+ "%" )
print("6: " + str(f) +"/" +str(i)+ "= "+ str(m)+ "%" ) 


