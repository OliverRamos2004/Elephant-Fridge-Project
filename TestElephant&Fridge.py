from fridge import Fridge  # Import your Fridge class from fridge.py
from elephant import elephant  # Import your elephant class from elephantanswer.py

"""
Project: Elephant and Fridge OOP Interaction

Description:
This script demonstrates the interaction between an Elephant and a Fridge using Object-Oriented Programming (OOP) in Python.
The project consists of two main classes:
1. Elephant: Defines an elephant with weight, height, and age, and provides actions such as eating, walking, and sleeping.
2. Fridge: Defines a fridge with brand and dimensions, and allows actions such as opening, closing, putting items in, and taking items out.

Instructions:
1. Run this script after ensuring that 'fridge.py' and 'elephantanswer.py' are in the same directory.
2. The script creates an instance of both the Fridge and the Elephant.
3. The user can:
    - Open the fridge using `my_fridge.open()`.
    - Check if the elephant can fit into the fridge based on its dimensions.
    - Put the elephant in the fridge if it fits using `my_fridge.put_in('elephant')`.
    - Close the fridge using `my_fridge.close()`.
    - Take the elephant out using `my_fridge.take_out('elephant')`.
4. Adjust the fridge's dimensions and elephant's attributes (weight, height, age) as needed.

Notes:
- Ensure the fridge is open before putting or removing items.
- The elephant's height must be smaller than the fridge's height to fit.
- The script provides real-time feedback and ensures that the fridge is properly managed (open/close status).

Example Commands:
    my_fridge.open()  # Open the fridge
    my_fridge.put_in("elephant")  # Put the elephant in the fridge
    my_fridge.close()  # Close the fridge
    my_fridge.take_out("elephant")  # Take the elephant out of the fridge

Author: [Oliver Ramos]
"""


# Create an elephant object
my_elephant = elephant(weight=10000, height=10, age=25)

# Create a fridge object
my_fridge = Fridge(brand="Samsung", dimensions=[15, 20, 30], capacity= 10000)  # Adjust the dimensions as needed

# Print the elephant and fridge details
print(my_elephant)
print(my_fridge)

# Open the fridge
my_fridge.open()

# Try to put the elephant in the fridge
if my_fridge.dimensions[0] > my_elephant.height:  # Check if the elephant fits in the fridge
    my_fridge.put_in("elephant")
else:
    print("The elephant doesn't fit in the fridge!")

# Close the fridge
my_fridge.close()

# Optionally, take the elephant out
my_fridge.open()
my_fridge.take_out("elephant")
