# Temperature Converter – Convert between Celsius, Fahrenheit, and Kelvin.

# print('Temperature Converter')
print('Temperature Converter\n',
    '1.celsius to fahrenheit\n',
    '2.fahrenheit to kelvin\n',
    '3.kelvin to celsius'
)
# Celsius to Fahrenheit
# °F = (°C * 9/5) + 32 
# Fahrenheit to Kelvin:
# K = (F - 32) * 5/9 + 273.15
# Kelvin to Celsius:
# °C = K - 273.15 
opt = int(input('choose the option: '))

temp = float(input('Enter the temperature: '))
if opt == 1:
    print('Converting celsius to fahrenheit!')
    f = (temp * 9/5) + 32
    print(f)
elif opt == 2:
    print('converting fahrenheit to kelvin!')
    k = (temp - 32) * 5/9 + 273.15
    print(k)
elif opt == 3:
    print('converting kelvin to celsius!')
    c = temp - 273.15
    print(c)
    



