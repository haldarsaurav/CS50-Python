# https://cs50.harvard.edu/python/2022/psets/0/tip/ ************* Click for the Question! 

def main(): # Function already given to us
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d): # Function to be coded
    tip_without_sign = d.replace("$", " ")
    return float(tip_without_sign)

def percent_to_float(p): # Function to be coded
    p_without_percent = p.replace("%", " ")
    p_converted = float(p_without_percent) / 100
    return float(p_converted)

main()