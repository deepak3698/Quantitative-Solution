
# Question:-  if A can complete a work in 10 days and B can complete the same work in 15 days then
# in how many days A and B together will complete that work.......

########## This Solution Format will work for every Question of this type #############

def LCM(x,y):
    for i in range(1, x * y + 1):
        if (i % x == 0 and i % y == 0):
            break
    return i

a=int(input("Enter the day in which A will complete their work.."))
b=int(input("Enter the day in which B will complete their work.."))

lcm=LCM(a,b)

val_1=lcm/a
val_2=lcm/b

result=lcm/(val_1+val_2)

if(result==int(result)):
    print(f"A and B will complete that work in {int(result)} days.")
else:
    print(" !!!!!!This can not be calculated in full day format!!!!!! ")
    print(f"A and B will complete that work in {int(result)} days.")








