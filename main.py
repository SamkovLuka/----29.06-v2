import random
#завдання 1
# vr = input("введіть математичний вираз: ")
# for i in str(vr):
#     vr.isdigit()
    
        
       

#завдання 2
list = []
for i in range(5):
    list.append(random.randint(-100,100))
print(list)
pos = 0
neg = 0
zeros = 0
min = list[0]
max = list[0]
for i in range(5):
    if list[1]>max:
        max=list[1]
        print(f"максимальне число - {max}")
    else:
        min=list[1]
        print(f"мінімальне число - {min}")
    if list[1]<0:
        neg+=1
        print(f"к-ість від'ємних чисел - {neg}")
    else:
        pos+=1
        print(f"к-ість додатних чисел - {pos}")
    if list[1]==0:
        zeros+=1
        print(f"к-ість нулів - {zeros}")