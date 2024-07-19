import random
import sys
from tabulate import tabulate


def number_of_days(cuisines_with_dishes):
    while True:
        try:
            number_of_days = input("""
How many days of random food schedule would you like to generate?
(Select from 1 - 7, 'q' to return to main menu)
""")

            if number_of_days.lower() == 'q' or number_of_days.lower() == 'quit':
                break

            number_of_days = int(number_of_days)

            if (1 <= number_of_days <= 7):
                scheduled_dishes = schedule_dishes_for_days(number_of_days, cuisines_with_dishes)
                sys.exit(tabulate(scheduled_dishes, headers=[
                    'Day', 'Dish', 'Cuisine'], tablefmt='outline'))
            else:
                raise ValueError
        except ValueError:
            print("\nInvalid: Invalid number of days\n")
            pass


def schedule_dishes_for_days(number_of_days, cuisines_with_dishes):

    schedule = []

    for day in range(1, number_of_days + 1):

        cuisine = random.choice(cuisines_with_dishes)

        dish = random.choice(cuisine['dishes']).title()

        schedule.append([f"Day {day}", dish, cuisine['name']])

    return schedule
