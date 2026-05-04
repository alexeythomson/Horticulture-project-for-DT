import json
import math
'''code to show profitability '''


#this makes a blueprint that all apples follow
#this blueprint is attributed to the objects which are the species of apples
#this makes the code future-proof if I add in more apple variety's
class Apple:
    def __init__(self, name, weight, v_quality, i_quality, s_time):
        self.name = name
        self.weight = weight
        self.v_quality = v_quality
        self.i_quality = i_quality
        self.s_time = s_time

    #__repr__ is useful for seeing the attributes of the apple
    #without the __repr__ the code will print "<__main__.Apple object at 0x000...>"
    def __repr__(self):
        return (f"{self.name}, {self.weight} grams, "
                f"{self.v_quality} out of 10, "
                f"{self.i_quality} out of 10, {self.s_time} out of 10")

    #this will calculate the score of the apple
    #this score will then be used to make an estimated value for the apple
    def calculate_apple_score(self):
        return (self.weight/1.25) + ((self.v_quality + self.i_quality + self.s_time) * 12.5)

#calculates the estimated values of apples
    def calculate_price_estimate(self):
        apple_score = self.calculate_apple_score()
        return apple_score / 250

#calculates customer interest out of 100 (caps at 100)
    def calculate_customer_interest(self):
        apple_score = self.calculate_apple_score()
        return (apple_score / 15) + (self.v_quality + self.i_quality
        + self.s_time) * 1.8777

#opens the file and by using 'with' it auto closes the file after doing the task
with open("resources/apples.json", 'r') as f:
    apple_data = json.load(f)

#creates an instance from the apple class for royal gala
#using ** checks the dictionary for the different attributes.
Royal_Gala = Apple(**apple_data['Royal_gala'])
print("price score:", Royal_Gala.calculate_apple_score())
print(Royal_Gala)
print(f"Estimated revenue per apple: ${Royal_Gala.calculate_price_estimate():.2f}")
print("Customer interest:", round((Royal_Gala.calculate_customer_interest()),2)
      ,"out of 100")