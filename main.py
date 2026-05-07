"""
Program to make user to find out which apple is more profitable
based on attributes of the apples.
"""

import json
import random

# this print is to separate the program from the top text
print()


class Apple:
    """Class to represent an apple"""
    def __init__(self, name, weight, v_quality, i_quality, s_time):
        """makes the blueprint for all objects (apples) under this class."""
        self.name = name
        self.weight = weight
        self.v_quality = v_quality
        self.i_quality = i_quality
        self.s_time = s_time

    #   __repr__ is useful for seeing the attributes of the apple
    #   without the __repr__ the code will print "<__main__.Apple object at 0x000...>"
    def __repr__(self):
        """Returns a string representation of the apple."""
        return (f"{self.name}, {self.weight:.1f} grams, "
                f"{self.v_quality:.1f} v_quality out of 10, "
                f"{self.i_quality:.1f} i_quality out of 10, "
                f"{self.s_time:.1f} s_quality out of 10.")

    def apple_variance(self):
        """This will randomly change the apple attributes to become
        different from what they are in the JSON file.
        This will make every interaction different from the last.
        """
        self.v_quality = min(10, self.v_quality + random.uniform(-1.5, 3))
        self.i_quality = min(10, self.i_quality + random.uniform(-1.5, 3))
        self.s_time = min(10, self.s_time + random.uniform(-1.5, 3))
        self.weight = round(self.weight * random.uniform(0.9, 1.15), 1)

    #   this will calculate the score of the apple
    #   this score will then be used to make an estimated value for the apple
    def calculate_apple_score(self):
        return (self.weight / 1.25) + ((self.v_quality + self.i_quality + self.s_time) * 12.5)

    # calculates the estimated values of apples
    def calculate_price_estimate(self):
        """calculates the estimated revenue per apple"""
        apple_score = self.calculate_apple_score()
        return apple_score / 250

    #   calculates customer interest out of 100 (caps at 100)
    def calculate_customer_interest(self):
        apple_score = self.calculate_apple_score()
        return (apple_score / 15) + (self.v_quality + self.i_quality
                                     + self.s_time) * 1.8777

    def cost_of_goods_sold(self):
        cogs = 0.5 + random.uniform(-0.075, 0.1)
        revenue = self.calculate_price_estimate()
        return revenue * cogs


# opens the file and by using 'with' it auto closes the file after doing the task
with open("resources/apples.json", 'r') as f:
    apple_data = json.load(f)

# creates an instance from the apple class for royal gala
# using ** checks the dictionary for the different attributes.
Royal_Gala = Apple(**apple_data['Royal_Gala'])
Granny_Smith = Apple(**apple_data['Granny_Smith'])

Granny_Smith.apple_variance()
Royal_Gala.apple_variance()

print(f"{Royal_Gala}")
print(f"Estimated revenue per apple: ${Royal_Gala.calculate_price_estimate():.2f}")
print("Customer interest:", round((Royal_Gala.calculate_customer_interest()), 2)
      , "out of 100")
print(f"cost of goods sold ${Royal_Gala.cost_of_goods_sold():.1f}")

print()

print(Granny_Smith)
print(f"Estimated revenue per apple: ${Granny_Smith.calculate_price_estimate():.2f}")
print("Customer interest:", round((Granny_Smith.calculate_customer_interest()), 2)
      , "out of 100")
print(f"cost of goods sold ${Granny_Smith.cost_of_goods_sold():.1f}")

