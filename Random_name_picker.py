import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
length=len(names)
#print(length)
select=random.randint(0,length-1)
finalnames=names[select]
print(f"{finalnames} is going to pay the bill for today")
