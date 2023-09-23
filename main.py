#highest common factor
#Samuel Wylie 12/9/2023

choice1 = int(input('What is the first number? '))
choice2 = int(input('What is the second number? '))


def highestcommonfactor(num1, num2):

    temporary = 1
    originalNum1 = num1
    originalNum2 = num2

    while True:

        # Finds which number is highest out of the two numbers
        if (num1 - num2) < (num2 - num1):
            lowernumber = num1
        else:
            lowernumber = num2

        if lowernumber == num1:
            temporary = num1
            num1 = num2
            num2 = temporary

        if num1 != num2 or num1 == (num2 * -1) or (num1 * -1) == num2:
            num1 = abs(num1 - num2)
        else:
            break

    print(f'Highest common factor of {originalNum1} and {originalNum2} is {num1}')


highestcommonfactor(choice1, choice2)
