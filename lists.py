#list=[10,12,20,35,65]
#total=sum(list)
#print(total)
total=0
#list=[10,12,20,35,65]
list=int(input("Enter list of numbers  " ))
for i in range(0,list):
    print(total,"+",list,end="")
    total=total+list
    print("=",total)
