from cuisine_preferences import add_cuisine, remove_cuisine
from dish_preferences import add_dish, remove_dish

# Mock cuisines_with_dishes for testing
cuisines_with_dishes = [
    {'name': 'Indian', 'dishes': ['samosa', 'naan']},
    {'name': 'Mexican', 'dishes': ['taco', 'burrito']}
]

def reset_cuisines():
    global cuisines_with_dishes
    cuisines_with_dishes = [
        {'name': 'Indian', 'dishes': ['samosa', 'naan']},
        {'name': 'Mexican', 'dishes': ['taco', 'burrito']}
    ]

def test_add_cuisine():
    reset_cuisines()
    assert add_cuisine(cuisines_with_dishes, 'pakistani') == "Cuisine 'pakistani' added successfully."
    assert add_cuisine(cuisines_with_dishes, 'indian') == "Cuisine 'indian' already exists."

def test_remove_cuisine():
    reset_cuisines()
    assert remove_cuisine(cuisines_with_dishes, 'indian') == "Cuisine 'indian' removed successfully."
    assert remove_cuisine(cuisines_with_dishes, 'italian') == "Cuisine 'italian' not found."

def test_add_dish():
    reset_cuisines()
    assert add_dish(cuisines_with_dishes, 'Indian', 'sambar') == "Added dish 'sambar' to Indian."
    assert add_dish(cuisines_with_dishes, 'Indian', 'samosa') == "Dish 'samosa' already exists in Indian."

def test_remove_dish():
    reset_cuisines()
    assert remove_dish(cuisines_with_dishes, 'Mexican', 'burrito') == "Removed dish 'burrito' from Mexican."
    assert remove_dish(cuisines_with_dishes, 'Indian', 'mutton korma') == "Dish 'mutton korma' not found in Indian."
