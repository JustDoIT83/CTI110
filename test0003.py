# CTI-110
# P3Sample - Display of if
# Kenneth Kleiner 
# 27 Sept 18
#
num1 = float(input('Enter first number: '))
num2 = float(input("Enter second number: "))
if (num1 > num2):
    result = num1 / num2
#    print('num1 / num2 =',result)
elif (num1 < num2):
    result = num1 * num2
#    print(result)
else:
    result = num1 ** num2
#    print(result)
print(format(result, '.4f'))
