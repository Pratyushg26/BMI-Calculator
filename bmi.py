height=float(input("Enter your height in centimeters: "))
weight=float(input("Enter your Weight in Kg: "))
height = height/100
BMI=weight/(height*height)
print("Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("Severely underweight")
	elif(BMI<=18.5):
		print("Underweight")
	elif(BMI<=25):
		print("Healthy")
	elif(BMI<=30):
		print("Overweight")
	else: print("Severely overweight")
else:("Please enter valid details")
