# Ice Cream Shop Application
# Author: Webbie
# Date: 2/2/2025

# Store our ice cream shop's menu items
flavors = ["vanilla", "caramel", "mint", "chocolate", "strawberry", "cookie dough"]  # List of available ice cream flavors
toppings = ["sprinkles", "nuts", "cherry"]  # List of available toppings
cone_types = ["cake", "sugar", "waffle"]  # List of available cone types
prices = {
    "scoop": 2.50,  # Price per scoop of ice cream
    "topping": 0.50,  # Price per topping
    "cone": 1.00  # Price per cone
}

def display_menu():
    """
    Displays the ice cream shop's menu, including available flavors, toppings, and prices.
    """
    print("\n=== Welcome to the Ice Cream Shop! ===")
    print("\nAvailable Flavors:")
    for flavor in flavors:  # Loop through the flavors list and display each flavor
        print(f"- {flavor}")
    
    print("\nAvailable Toppings:")
    for topping in toppings:  # Loop through the toppings list and display each topping
        print(f"- {topping}")
    
    print("\nAvailable Cone Types:")
    for cone in cone_types:  # Loop through the cone types list and display each cone type
        print(f"- {cone}")
    
    print("\nPrices:")
    print(f"Scoops: ${prices['scoop']:.2f} each")  # Display the price per scoop
    print(f"Toppings: ${prices['topping']:.2f} each")  # Display the price per topping
    print(f"Cone: ${prices['cone']:.2f}")  # Display the price per cone

def get_flavors():
    """
    Prompts the user to select the number of scoops and their desired flavors.
    Returns the number of scoops and a list of chosen flavors.
    """
    chosen_flavors = []  # List to store the user's chosen flavors
    attempts = 0  # Counter to track invalid attempts for number of scoops

    # Loop to get the number of scoops from the user
    while True:
        try:
            num_scoops = int(input("\nHow many scoops would you like? (1-3): "))  # Prompt for number of scoops
            if 1 <= num_scoops <= 3:  # Validate that the number of scoops is between 1 and 3
                break
            print("Please choose between 1 and 3 scoops.")  # Error message for invalid input
        except ValueError:  # Handle non-numeric input
            print("Please enter a number.")
        attempts += 1
        if attempts >= 3:  # Exit if too many invalid attempts
            print("Too many invalid attempts. Exiting.")
            return 0, []  # Return 0 scoops and an empty list if the user fails to provide valid input
    
    # Loop to get the flavor for each scoop
    print("\nFor each scoop, enter the flavor you'd like:")
    print("Available flavors:", ", ".join(flavors))  # Display available flavors
    for i in range(num_scoops):  # Loop for each scoop
        attempts = 0  # Counter to track invalid attempts for flavor selection
        while True:
            flavor = input(f"Scoop {i+1}: ").lower()  # Prompt for flavor input
            if flavor in flavors:  # Check if the flavor is in the available flavors list
                chosen_flavors.append(flavor)  # Add the flavor to the chosen_flavors list
                break
            print("Sorry, that flavor isn't available. Available flavors:", ", ".join(flavors))  # Error message for invalid flavor
            attempts += 1
            if attempts >= 3:  # Exit if too many invalid attempts
                print("Too many invalid attempts. Exiting.")
                return 0, []  # Return 0 scoops and an empty list if the user fails to provide valid input
    
    return num_scoops, chosen_flavors  # Return the number of scoops and the list of chosen flavors

def get_toppings():
    """
    Prompts the user to select toppings until they type 'done'.
    Returns a list of chosen toppings.
    """
    chosen_toppings = []  # List to store the user's chosen toppings
    attempts = 0  # Counter to track invalid attempts for toppings

    # Loop to get toppings from the user
    print("Available toppings:", ", ".join(toppings))  # Display available toppings
    while True:
        topping = input("\nEnter a topping (or 'done' if finished): ").lower()  # Prompt for topping input
        if topping == 'done':  # Exit the loop if the user is done adding toppings
            break
        if topping in toppings:  # Check if the topping is in the available toppings list
            chosen_toppings.append(topping)  # Add the topping to the chosen_toppings list
            print(f"Added {topping}!")  # Confirmation message
        else:
            print("Sorry, that topping isn't available. Available toppings:", ", ".join(toppings))  # Error message for invalid topping
            attempts += 1
            if attempts >= 3:  # Exit if too many invalid attempts
                print("Too many invalid attempts. Exiting.")
                break
    
    return chosen_toppings  # Return the list of chosen toppings

def get_cone_type():
    """
    Prompts the user to select a cone type.
    Returns the chosen cone type.
    """
    attempts = 0  # Counter to track invalid attempts for cone type selection

    # Loop to get the cone type from the user
    while True:
        cone = input("\nEnter the cone type (cake, sugar, waffle): ").lower()  # Prompt for cone type input
        if cone in cone_types:  # Check if the cone type is in the available cone types list
            return cone  # Return the chosen cone type
        print("Sorry, that cone type isn't available. Available cone types:", ", ".join(cone_types))  # Error message for invalid cone type
        attempts += 1
        if attempts >= 3:  # Exit if too many invalid attempts
            print("Too many invalid attempts. Exiting.")
            return None  # Return None if the user fails to provide valid input

def calculate_total(num_scoops, num_toppings, cone_type):
    """Calculates the total cost of the order"""
    scoop_cost = num_scoops * prices["scoop"]
    topping_cost = num_toppings * prices["topping"]
    cone_cost = prices["cone"] if cone_type else 0  # Add cone cost if a cone type is selected
    total = scoop_cost + topping_cost + cone_cost
    
    # Apply 10% discount for orders over $10
    if total > 10:
        total *= 0.90  # Apply 10% discount
        print("\nYou've received a 10% discount for orders over $10!")
    
    return total

def print_receipt(num_scoops, chosen_flavors, chosen_toppings, cone_type):
    """Prints a nice receipt for the customer"""
    print("\n=== Your Ice Cream Order ===")
    for i in range(num_scoops):
        print(f"Scoop {i+1}: {chosen_flavors[i].title()}")
    
    if chosen_toppings:
        print("\nToppings:")
        for topping in chosen_toppings:
            print(f"- {topping.title()}")
    
    if cone_type:
        print(f"\nCone Type: {cone_type.title()}")
    
    total = calculate_total(num_scoops, len(chosen_toppings), cone_type)
    print(f"\nTotal: ${total:.2f}")
    
    # Save order to file
    try:
        with open("daily_orders.txt", "a") as file:
            file.write(f"\nOrder: {num_scoops} scoops - ${total:.2f}")
    except IOError as e:
        print(f"Error saving order to file: {e}")

def main():
    """Runs our ice cream shop program"""
    while True:
        display_menu()
        num_scoops, chosen_flavors = get_flavors()
        if num_scoops == 0:
            print("No valid flavors selected. Exiting.")
            break
        chosen_toppings = get_toppings()
        cone_type = get_cone_type()
        print_receipt(num_scoops, chosen_flavors, chosen_toppings, cone_type)
        
        another_order = input("\nWould you like to place another order? (yes/no): ").lower()
        if another_order != 'yes':
            print("Thank you for visiting the Ice Cream Shop!")
            break

if __name__ == "__main__":
    main()
