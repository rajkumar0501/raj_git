from tabulate import tabulate


def add_remove_cuisine(cuisines_with_dishes):
    while True:
        try:
            display_cuisines(cuisines_with_dishes)
            choose_cuisine = input("""
Do you want to add or remove a cuisine?
('y' to add, 'n' to remove, 'q' to return to main menu)
""")

            if choose_cuisine.lower() == 'q' or choose_cuisine.lower() == 'quit':
                break
            else:
                cuisine_name = input("Name of the cuisine you want to add or remove? ")
                if choose_cuisine.lower() == 'y' or choose_cuisine.lower() == 'yes':
                    print(add_cuisine(cuisines_with_dishes, cuisine_name))
                    display_cuisines(cuisines_with_dishes)
                elif choose_cuisine.lower() == 'n' or choose_cuisine.lower() == 'no':
                    print(remove_cuisine(cuisines_with_dishes, cuisine_name))
                    display_cuisines(cuisines_with_dishes)
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
                    break
            break
        except ValueError:
            break


def display_cuisines(cuisines_with_dishes):
    cuisines = [[cuisine["name"]] for cuisine in cuisines_with_dishes]

    print(tabulate(cuisines, headers=['Cuisines'], tablefmt='outline'))


def add_cuisine(cuisines_with_dishes, cuisine_name):
    if any(cuisine['name'] == cuisine_name.capitalize() for cuisine in cuisines_with_dishes):
        return (f"Cuisine '{cuisine_name}' already exists.")
    else:
        cuisines_with_dishes.append({'name': cuisine_name.capitalize(), 'dishes': []})
        return (f"Cuisine '{cuisine_name}' added successfully.")


def remove_cuisine(cuisines_with_dishes, cuisine_name):
    if any(cuisine['name'] == cuisine_name.capitalize() for cuisine in cuisines_with_dishes):
        cuisines_with_dishes[:] = [
            cuisine for cuisine in cuisines_with_dishes if cuisine['name'] != cuisine_name.capitalize()]
        return (f"Cuisine '{cuisine_name}' removed successfully.")
    else:
        return (f"Cuisine '{cuisine_name}' not found.")
