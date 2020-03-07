choice = int(input("1 - C 2 - F"))

if choice == 2:
    temp = int(input("Fahrenheit: "))
    double_tempC = (temp - 32) * 5 / 9
    print(double_tempC)
elif choice == 1:
    temp = int(input("Celcius: "))
    fahren = (temp * 9 / 5) + 32
    print(fahren)
    
#proverit etu zadachu