# Write function bmi that calculates body mass index (bmi = weight / height ^ 2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    calculation = weight / height**2
    if calculation <= 18.5:
        return "Underweight"
    if calculation <= 25.:
        return "Normal"
    if calculation <= 30.:
        return "Overweight"
    else:
        return "Obese"