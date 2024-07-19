from tabulate import tabulate


def add_remove_dish(cuisines_with_dishes):
    while True:
        try:
            display_cuisines(cuisines_with_dishes)
            selected_cuisine = input("""
Select(Type) one of the cuisines from above table to add the dishes
(press'q' to return to main menu)
""")

            cuisine_names = [cuisine['name'] for cuisine in cuisines_with_dishes]

            if selected_cuisine.lower() == 'q' or selected_cuisine.lower() == 'quit':
                break
            elif selected_cuisine.capitalize() not in cuisine_names:
                print("Selected cuisine not in the list of cuisines")
                pass
            else:
                q5 = input("Would you like to 'add' or 'remove' a dish? ")
                if (q5.lower() == 'add'):
                    while True:
                        dish_add = input("Enter a dish (or 'done' to finish): ")
                        if dish_add.lower() == 'done':
                            break
                        print(add_dish(cuisines_with_dishes, selected_cuisine, dish_add))
                        display_cuisine_dishes(cuisines_with_dishes, selected_cuisine)
                elif (q5.lower() == 'remove'):
                    while True:
                        dish_remove = input("Enter a dish (or 'done' to finish): ")
                        if dish_remove.lower() == 'done':
                            break
                        print(remove_dish(cuisines_with_dishes, selected_cuisine, dish_remove))
                        display_cuisine_dishes(cuisines_with_dishes, selected_cuisine)
                else:
                    print("Invalid input: Either needs to add or remove dish")
                    break
            break
        except ValueError:
            break


def display_cuisines(cuisines_with_dishes):
    cuisines = [[cuisine["name"]] for cuisine in cuisines_with_dishes]

    print(tabulate(cuisines, headers=['Cuisines'], tablefmt='outline'))


def display_cuisine_dishes(cuisines_with_dishes, cuisine_name):
    for cuisine in cuisines_with_dishes:
        if cuisine['name'] == cuisine_name.capitalize():
            print(tabulate([[dish] for dish in cuisine['dishes']],
                  headers=[cuisine_name.capitalize()], tablefmt='outline'))
            return


def add_dish(cuisines_with_dishes, cuisine_name, dish_add):
    for cuisine in cuisines_with_dishes:
        if cuisine['name'] == cuisine_name.capitalize():
            if dish_add.lower() not in cuisine['dishes']:
                cuisine['dishes'].append(dish_add.lower())
                return (f"Added dish '{dish_add}' to {cuisine_name}.")
            else:
                return (f"Dish '{dish_add}' already exists in {cuisine_name}.")


def remove_dish(cuisines_with_dishes, cuisine_name, dish_remove):
    for cuisine in cuisines_with_dishes:
        if cuisine['name'] == cuisine_name.capitalize():
            if dish_remove.lower() in cuisine['dishes']:
                cuisine['dishes'].remove(dish_remove.lower())
                return (f"Removed dish '{dish_remove}' from {cuisine_name}.")
            else:
                return (f"Dish '{dish_remove}' not found in {cuisine_name}.")
