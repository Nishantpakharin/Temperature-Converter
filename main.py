def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print('Temperature converter\n',
          '1.celsius to fahrenheit\n',
          '2.celsius to kelvin\n',
          '3.fahrenheit to celsius\n',
          '4.fahrenheit to kelvin\n',
          '5.kelvin to celsius\n',
          '6.kelvin to fahrenheit\n'
          )
    
    choice = int(input('Enter your choice(1-6): '))

    if choice == 1:
        celsius = float(input('Enter the temperature in Celsius: '))
        print(f'Celsius to Fahrenheit: {celsius_to_fahrenheit(celsius)}')
    elif choice == 2:
        celsius = float(input('Enter the temperature in Celsius: '))
        print(f'Celsius to kelvin: {celsius_to_kelvin(celsius)}')
    elif choice == 3:
        fahrenheit = float(input('Enter the temperature in Fahrenheit: '))
        print(f'Fahrenheit to celsius: {fahrenheit_to_celsius(fahrenheit)}')
    elif choice == 4:
        fahrenheit = float(input('Enter the temperature in Fahrenheit: '))
        print(f'Fahrenheit to kelvin: {fahrenheit_to_kelvin(fahrenheit)}')
    elif choice == 5:
        kelvin = float(input('Enter the temperature in Kelvin: '))
        print(f'Kelvin to Celsius: {kelvin_to_celsius(kelvin)}')
    elif choice == 6:
        kelvin = float(input('Enter the temperature in Kelvin: '))
        print(f'Kelvin to Fahrenheit: {kelvin_to_fahrenheit(kelvin)}')
    else:
        print('Invalid choice!')

if __name__ == "__main__":
    main()        