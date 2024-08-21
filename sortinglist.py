list=[int(x) for x in input("Enter list of numbers  ").split()]
list.sort()
print("Ascending")
print(list)
list.sort(reverse=True)
print("Descending")
print(list)