# MealMap

A CLI tool to randomly suggest your weekly dinner schedule

[Video demo](https://youtu.be/KF-lEw5GONw)

---

## Folder Contents

project.py: Contains the main function and other necessary functions to run the menu.
menu.py: Contains functions to view or add a new menu.
cuisine_preferences.py: Contains functions to add or remove a cuisine.
dish_preferences.py: Contains functions to add or remove a dish from a cuisine.
schedule.py: Contains functions to generate a meal schedule for a given number of days.
requirements.txt: Lists all pip-installable libraries used for this project.
test_project.py: Contains test functions for cuisine_preferences.py and dish_preferences.py.

---

## Libraries Used

- `tabulate` : For generating the output and organised in a table in the Terminal
- `pytest` : For Functional Testing
- `random` : For generating random selections

---

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install the packages `tabulate` and `pytest`

To install tabulate, type

```
$ pip install tabulate
```

To have a quick summary of Tabulate's functionalities, type

```
$ python -m tabulate
```

To install Pytest, type

```
$ pip install pytest

```
- By default, the Food Scheduler initializes with a pre-defined set of cuisines and dishes.
- When running the test cases, the user is presented with a series of tests covering various functions of the Food Scheduler.
- Each test case verifies the behavior and functionality of different functions within the Food Scheduler module.
- The tests are designed to ensure that the functions correctly handle inputs, update data structures, and produce the expected output.
- The test cases cover a range of scenarios, including adding and removing dishes from cuisines, generating a meal schedule for a specified number of days, and more.
- Users can also add or remove cuisines from the list of available cuisines using the respective commands.


---

## Documentation

### project.py Functions (excluding main)

```python
def handle_choice(choice, active_cuisines):
```

**Description:**

- Handles the choice by error checking.


```python
def get_user_choice():
```

**Description:**

- Gets the choice of the user from the menu.


```python
def display_menu():
```

**Description:**

- Displays the main menu and handles user input to execute the appropriate commands.


```python
def select_menu():
```

**Description:**

- Prompts the user to view a pre-existing menu or create a new one.


```python
def display_existing_menu():
```

**Description:**

- Displays the current menu in a formatted table using tabulate.


```python
def input_cuisine_details():
```

**Description:**

- Prompts the user to enter details for a new cuisine.

**Returns:**

- `dict`: A `list` containing the cuisine name and a list of dishes.


```python
def menu_new():
```

**Description:**

- Prompts the user to enter new cuisines and their dishes, and displays them in a formatted table.


```python
def add_remove_cuisine():
```

**Description:**

- Prompts the user to add or remove a cuisine.


```python
def add_remove_dish():
```

**Description:**

- Prompts the user to add or remove a dish from a selected cuisine.


```python
def display_cuisines():
```

**Description:**

- Displays the list of available cuisines in a formatted table using tabulate.


```python
def display_cuisine_dishes(cuisine_name):
```

**Description:**

- Displays the list of selected cuisine with it's dishes in a formatted table using tabulate.


```python
def add_cuisine(cuisine_name):
```

**Description:**
- Adds a new cuisine to the list of available cuisines.

**Args:**
- `cuisine_name` (`str`): The name of the new cuisine to be added.

**Returns:**
- `str`: Confirmation `str` message of the added cuisine.


```python
def remove_cuisine(cuisine_name):
```

**Description:**
- Removes a cuisine from the list of available cuisines.

**Args:**
- `cuisine_name` (`str`): The name of the new cuisine to be removed.

**Returns:**
- `str`: Confirmation `str` message of the removed cuisine.


```python
def add_dish(cuisine_name, new_dish):
```

**Description:**

- Adds a new dish to the specified cuisine if it doesn't already exist.

**Args:**

- `cuisine_name` (`str`): The name of the cuisine.
- `new_dish` (`str`): The name of the dish to be added.

**Returns:**

- `str`: Confirmation `str` message of the added dish


```python
def remove_dish(cuisine_name, dish_to_remove):
```

**Description:**

- Removes a dish from the specified cuisine if it exists.

**Args:**

- `cuisine_name` (`str`): The name of the cuisine.
- `dish_to_remove` (`str`): The name of the dish to be removed.

**Returns:**

- `str`: Confirmation `str` message of the removed dish.


```python
def number_of_days():
```

**Description:**

- Prompts the user to enter the number of days for generating a meal schedule and displays the schedule.

**Returns:**

- `list`: A `list` of scheduled meals for the given number of days.


```python
def schedule_dishes_for_days(number_of_days):
```

**Description:**

- Generates a meal schedule for a given number of days using random selection.

**Args:**

- `number_of_days` (`int`): The number of days to generate the schedule for.

**Returns:**

- `list`: A `list` of scheduled meals for the given number of days.

---

## Usage

Use [python](https://www.python.org/) to run the application

````

$ python project.py

```

Use [pytest](https://docs.pytest.org/en/7.2.x/) to test the application

```

$ pytest test_project.py

```

---

## Commands List

```

View or Add Cuisines - View the current menu or create a new menu
Add or Remove a a Cuisine - Add or Remove a cuisine
Add or Remove a Dish to a Cuisine - Add or Remove a new dish to the cuisine
Schedule Dishes for Days - Generate a meal schedule for required number of days
Exit - Exit the program

```
```
```
