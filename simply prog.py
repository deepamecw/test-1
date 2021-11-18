"""
a = int(input("enter the value of A:"))
b = int(input("enter the value of B: "))
if a > b:
    print(a, " is greater")
elif a < b:
    print(a,"is lesser than ",b)
else:
    print(a, " is equal to  b")

i = 1
while i < 11:
    print(i)
    i += 2



for x in "abcdefghijklmnopqrstuvwxyz":
    print(x)
      
fruits = ("apple", "grapes", "banana","pineapple")
for x in fruits:
    print(x)#
    if x == "banana":
        break
    
fruits = ("apple", "grapes", "banana","pineapple")
for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(1,11):
     print(x)
         
  """
for x in[0, 1, 2]:
    pass