def newtons_second_law():
    print("The newton's second formulae is Mass * Acceleration")
    Mass = float(input("Enter the mass of the object (in Kilogram): "))
    Acceleration = float(input("Enter the accelaration of the object (in meters per second square): "))
    Force = Mass * Acceleration
    print("The force at which the object is moving is: ", {Force})

def ohms_law():
    print("The ohms law formulae goes as current * Time")
    Current = float(input("Enter the current flowing through the circuit: "))
    Resistance = float(input("Enter the resistance of the circuit: "))
    Voltage = Current * Resistance
    print("The voltage flowing through the circuit is: ", {Voltage})

def kinectic_energy():
    print("Kinectic energy of a body is calculated 1/2 * mass * (velocity^2)")
    Mass = float(input("Enter the mass of the object (in Kilogram): "))
    Velocity = float(input("Enter the speed at which the object is moving (in meters per second): "))
    kinectic_energy = 0.5 * Mass * (Velocity * Velocity)
    print("The kinectic energy the body possesses is:", {kinectic_energy})

def velocity():
    Distance = float(input("Enter the distance travelled by the body: "))
    Time = float(input("Enter the time taken to cover the distance: "))
    velocity = Distance / Time
    print("The velocity the object is moving at is: ", {velocity})

def impulsive_momentum():
    Force  = float(input("Enter the force of the object: "))
    Time = float(input("Enter the time taken to cover the distance: "))
    impulsive_momentum = Force * Time
    print("The impulsive momentum of the object at an instance is: ",  {impulsive_momentum})

#--------------------------------------------

#                   main                   

#--------------------------------------------

def main():
    print("1. Newton's second law")
    print("2. ohm's law")
    print("3. kinectic energy")
    print("4. Velocity")
    print("5. Impulsive momentum")
    choice = input("Enter the option of your choice? ")

    if choice == "1":
        newtons_second_law()
    elif choice == "2":
        ohms_law()
    elif choice == "3":
        kinectic_energy()
    elif choice == "4":
        velocity()
    elif choice == "5":
        impulsive_momentum()
    else:
        print("Invalid choice, please select a valid option.")

main()