height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
height_=float(height)
weight_=float(weight)
bmi=int(weight_/(height_**2))
print(weight+" % "+"("+ height +" * "+ height+")"+" = "+str(bmi))
