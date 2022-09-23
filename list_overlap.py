import random
list1_length=random.randint(0,20)
list2_length =random.randint(0,20)

lst1=[]
lst2=[]


for i in range(list1_length):
    lst1.append(random.randint(1,i+1))
print(lst1)

for i in range(list2_length):
    lst2.append(random.randint(1,i+1))
print(lst2)
result=[]
for element in lst1:
        if element in lst2:
            if element in result:
                continue
            else:
                result.append(element)
            
print(result)








