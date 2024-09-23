def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollars_str):
    # Remove the leading $
    amount_str = dollars_str 
    
    # Convert the remaining string to float
    amount_float = float(amount_str)

    return amount_float
    
def percent_to_float(percent_str):
    # Remove the trailing %
    percent_str = percent_str.rstrip('%')
    
    # Convert the remaining string to float and divide by 100
    percent_float = float(percent_str) / 100.0
    
    return percent_float


main()