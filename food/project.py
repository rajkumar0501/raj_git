from cuisine_preferences import add_remove_cuisine
from cuisines import cuisines_with_dishes
from dish_preferences import add_remove_dish
from menu import select_menu
from schedule import number_of_days
from tabulate import tabulate


def main():

    print("""
    Hello, Welcome to MealMap - A Weekly Dinner Scheduler""")

    active_cuisines = cuisines_with_dishes

    while True:
        display_menu()
        choice = get_user_choice()
        active_cuisines = handle_choice(choice, active_cuisines)
        if choice == 5:
            break


def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")


def handle_choice(choice, active_cuisines):
    if choice == 1:
        return select_menu()
    elif choice == 2:
        add_remove_cuisine(active_cuisines)
    elif choice == 3:
        add_remove_dish(active_cuisines)
    elif choice == 4:
        number_of_days(active_cuisines)
    elif choice == 5:
        print("\nExiting the program\n")
        return None


def display_menu():
    menu = """
    1. View or Add Cuisines
    2. Add or Remove a Cuisine
    3. Add or Remove a Dish to a Cuisine
    4. Schedule Dishes for Days
    5. Exit
    """
    print(menu)


if __name__ == "__main__":
    main()
