import random
x = 0
cont = 0
while True:
    for i in range (0,10):
        y = random.randint(0,1)
        x += y
        print("Número aleatório:",y)
        print("X em i =",i,"é",x)
    if(x == 10):
        break
    else: 
        print("\n!!!PROXIMA TENTATIVA!!!\n")
        x = 0
        cont += 1
print("X:",x)
print("Contágem:",cont)