# Program Name: Lab4.py
# Course: IT1114/Section XXX
# Student Name: Daniel Urdaneta
# Assignment Number: Lab4
# Due Date: 09/29/24
# Purpose: This program allows a user to calculate the cost of a resort vacation
# Resources used:

# Function to calculate room cost
def roomCost(nights, room_type):
    if room_type == 1:
        return nights * 375  # Two Queen Beds
    elif room_type == 2:
        return nights * 350  # One King Bed
    elif room_type == 3:
        return nights * 525  # Queen Suite
    elif room_type == 4:
        return nights * 475  # King Suite


# Function to calculate meal cost (with gratuity)
def mealCost(brunches, dinners):
    brunch_total = brunches * 25
    dinner_total = dinners * 75
    meal_total = brunch_total + dinner_total
    gratuity = 0.15 * meal_total  # 15% gratuity
    return meal_total + gratuity


# Function to calculate excursion cost
def excursionCost(picnic, snorkeling, hike, boat_dinner, people):
    total = 0
    if picnic:
        total += 50
    if snorkeling:
        total += 25 * people  # Snorkeling is per person
    if hike:
        total += 17 * people  # Guided Hike is per person
    if boat_dinner:
        total += 200
    return total


# Main program
def main():
    # Get input from the user
    nights = int(input("Number of nights: "))
    people = int(input("Number of people: "))

    print("Room Types:\n(1) - Two Queen Beds\n(2) - One King Bed\n(3) - Queen Suite\n(4) - King Suite")
    room_type = int(input("Select Type: "))

    brunches = int(input("How many Brunches: "))
    dinners = int(input("How many Dinners: "))

    picnic = input("Picnic? (y/n): ").lower() == 'y'
    snorkeling = input("Snorkeling? (y/n): ").lower() == 'y'
    hike = input("Guided Hike? (y/n): ").lower() == 'y'
    boat_dinner = input("Boat Dinner? (y/n): ").lower() == 'y'

    # Calculate costs
    room_total = roomCost(nights, room_type)
    meal_total = mealCost(brunches, dinners)
    excursion_total = excursionCost(picnic, snorkeling, hike, boat_dinner, people)

    # Calculate the grand total
    grand_total = room_total + meal_total + excursion_total

    # Display results
    print(f"\nRoom Cost: ${room_total}")
    print(f"Meal Cost: ${meal_total}")
    print(f"Excursion Cost: ${excursion_total}")
    print(f"Total Cost: ${grand_total}")


# Call the main function
if __name__ == "__main__":
    main()
