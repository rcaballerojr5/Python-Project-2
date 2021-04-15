# Enter length and weight
length = float(input(' enter length in meters: '))
weight = float(input(' enter weight in kgs: '))
# formula
def BMI(length, weight):
    bmi = weight/(length*length)
    if (bmi < 16):
        return 'Severely underweight', bmi

    elif (bmi >= 16 and bmi < 18.5):
        return 'underweight', bmi

    elif (bmi >= 18.5 and bmi < 25):
        return 'healthy', bmi

    elif (bmi >= 25 and bmi < 30):
        return ' overweight', bmi

    elif (bmi >= 30):
        return 'obese', bmi
# quote for input
quote, bmi = BMI(length, weight)
print('Your BMI is: {} and you are: {}'.format(bmi, quote))
