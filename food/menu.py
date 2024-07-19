from cuisines import cuisines_with_dishes
from tabulate import tabulate


def select_menu():
    while True:
        try:
            q1 = input("""
Would you like to view pre-existing menu or create a new menu? y/n
('y' to view, 'n' to add, 'q' to return to main menu)
""")
            if q1.lower() == 'y' or q1.lower() == 'yes':
                display_existing_menu(cuisines_with_dishes)
                return cuisines_with_dishes
            elif q1.lower() == 'n' or q1.lower() == 'no':
                return menu_new()
            elif q1.lower() == 'q' or q1.lower() == 'quit':
                return
            else:
                raise ValueError
        except ValueError:
            print("Invalid input: Should say yes or no")
            pass


def display_existing_menu(cuisines_with_dishes):
    table_data = []
    for cuisine in cuisines_with_dishes:
        table_data.append([cuisine['name'], ', '.join(cuisine['dishes'])])

    print(tabulate(table_data, headers=['Cuisine', 'Dishes'], tablefmt='outline'))


def input_cuisine_details():
    cuisine_name = input("Enter the name of the cuisine: ")
    dishes = []
    while True:
        dish = input("Enter a dish (or 'done' to finish): ")
        if dish.lower() == 'done':
            break
        dishes.append(dish)
    return {'name': cuisine_name, 'dishes': dishes}


def menu_new():
    new_cuisines_with_dishes = []
    number_of_cuisines = int(input("""
How many cuisines do you want to enter?
"""))

    for _ in range(number_of_cuisines):
        cuisine_details = input_cuisine_details()
        new_cuisines_with_dishes.append(cuisine_details)

    print("\nCuisines with their dishes:")
    for cuisine in new_cuisines_with_dishes:
        print(f"{cuisine['name']}: {', '.join(cuisine['dishes'])}")

    formatted_data = [(cuisine['name'], ', '.join(cuisine['dishes']))
                      for cuisine in new_cuisines_with_dishes]
    print("\nFormatted Cuisines with Dishes:")
    print(tabulate(formatted_data, headers=['Cuisine', 'Dishes'], tablefmt='outline'))

    return new_cuisines_with_dishes
