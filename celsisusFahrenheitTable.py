print("Celsius     Fahrenheit")
print("-------------------------")
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print('{0}     {1}'.format(celsius,fahrenheit))
