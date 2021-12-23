import math
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
list=[]
squaredvalues =[] 
# iterating each number in list
for num in range(start, end + 1):
    list.append(num)
print(list)
n=len(list)
print("the length of the list is\n", n)
for i in list:
    root = math.sqrt(i)
    if int(root + 0.5) ** 2 == i:
        # print(i, "is a  square")
         squaredvalues.append(i)        
print("the suared values of the list are\n", squaredvalues)
if list.count(57)!= 0:
    print ("57 is in the list")





