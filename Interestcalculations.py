def Simpleinterest(P,T,R):
     Result=(P*T*R)/100
     print(Result)
def Compoundinterest(P,T,R):
     Result=P*(pow((1+R/100),T))
     print(Result)
P=int(input("Enter Principal Amount: "))
R=int(input("Enter Rate of interest:  "))
T=int(input("Enter Time Period : "))
print("Simple Interest")
Simpleinterest(P,T,R)
print("Compund Interest")
Compoundinterest(P,T,R)