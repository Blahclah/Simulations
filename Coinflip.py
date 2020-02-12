import random

numFlips = int(input("How many flips? "))

flips = [0]*2

i = 0

while (i< numFlips):
    flip = random.randint(0,1)
    flips[flip-1] +=1

  
    i += 1


   

    

for i in  range(len(flips)):
    print(f"{i}: {flips[i]}/{numFlips}  = {flips[i]/numFlips*100}%")





