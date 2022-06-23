# https://cs50.harvard.edu/python/2022/psets/0/einstein/ ************* Click for the Question! 

mass = int(input("Enter the Mass(in Kgs) "))    # Ask user for a mass
light_speed = 300000000
print("The Mass is = ", mass)
energy = mass * (light_speed ** 2)  # Calculate the Energy in Joules
print("The Energy of = ", mass, "Kgs of mass is = ", energy, "Joules")   # Print the result