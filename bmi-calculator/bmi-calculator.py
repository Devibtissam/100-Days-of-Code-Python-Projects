weight=float(input('enter your weight in kg:'))
height=float(input('enter your height in m:'))

bmi=weight / height ** 2
bmi_as_int=round(bmi,2)
print(bmi_as_int)

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

if bmi_as_int < 18.5:
    print(f"Your BMI is {bmi_as_int}, you are underweight")
elif bmi_as_int < 25:
    print(f"Your BMI is {bmi_as_int}, you have a normal weight")
elif bmi_as_int < 30:
    print(f"Your BMI is {bmi_as_int}, you are slightly overwight")
elif bmi_as_int < 35:
    print(f"Your BMI is {bmi_as_int}, your are obese")
else:
    print(f"Your BMI is {bmi_as_int}, you are clinically obese")
