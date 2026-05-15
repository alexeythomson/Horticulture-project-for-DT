"""
Program to make the end user work out the profitability of an apple by using a formula provided to them,
and then they will have to figure out which apple is more profitable.
"""
import json
import random
import time


def terminal_clear():
    print("\n" * 20)


class Apple:
    """Class to represent an apple"""

    def __init__(self, name, weight, v_quality, i_quality, s_time):
        """makes the blueprint for all objects (apples) under this class."""

        self.name = name
        self.weight = weight
        self.v_quality = v_quality
        self.i_quality = i_quality
        self.s_time = s_time
        self.cogs_rate = 0.5 + random.uniform(-0.05, 0.1)
    # I added in the cogs_rate here because I found a bug that made
    # it so the cost of goods rerolled twice causing the answers to become wrong

    def __repr__(self):
        """Returns a string representation of the apple. Also without the __repr__
         the code will print "<__main__.Apple object at 0x000...>"""""

        return (f"{self.name}\n attributes: {self.weight:.1f} grams, "
                f"{self.v_quality:.1f} v_quality out of 10, "
                f"{self.i_quality:.1f} i_quality out of 10, "
                f"{self.s_time:.1f} s_quality out of 10.")
    #   __repr__ is useful for seeing the attributes of the apple
    #   without the __repr__ the code will print "<__main__.Apple object at 0x000...>"

    def apple_variance(self):
        """This will randomly change the apple attributes to become
        different from what they are in the JSON file.
        This will make every interaction different from the last.
        """
        self.v_quality = min(10, self.v_quality + random.uniform(-1.5, 4))
        self.i_quality = min(10, self.i_quality + random.uniform(-1.5, 4))
        self.s_time = min(10, self.s_time + random.uniform(-1.5, 4))
        self.weight = round(self.weight * random.uniform(0.9, 1.15), 1)

    def calculate_apple_score(self):
        """this calculates a score for the apple which the price estimate and consumer interest
        calculations will work off of, this helps reduce unnecessary code"""

        return (self.weight / 1.25) + ((self.v_quality + self.i_quality + self.s_time) * 12.5)

    def calculate_price_estimate(self):
        """calculates the estimated revenue per apple"""

        apple_score = self.calculate_apple_score()
        return apple_score / 250

    def calculate_customer_interest(self):
        """Calculates the customer interest on an apple by using the apple score together with
        a multiple that will increase depending on certain attributes.
        For this code the *1.877 is so specific because it makes sure the customer interest score
        doesn't go over 100 out of 100 causing an error."""

        apple_score = self.calculate_apple_score()
        return (apple_score / 15) + (self.v_quality + self.i_quality
                                     + self.s_time) * 1.8777

    def cost_of_goods_sold(self):
        """this is a calculation to figure out the total production cost of the specific apple,
        it's made to give a different percentage each time to simulate the difference in production cost
        in different orchards"""
        revenue = self.calculate_price_estimate()
        return revenue * self.cogs_rate

    def profitability_score(self):
        """this is a calculation to see how profitable an apple will be, with 1 being profitable and
        0.99... or under being unprofitable. The reason I did this instead of total profit is because
        this way it's easier to factor in variables such as customer preference for the apple which isn't
        a monetary factor but instead influences how many people are willing to buy the apple.
        This also makes it better for the end user because they are learning more in depth about what
        affects profitability instead of just taking away production cost from revenue from an apple."""

        return (self.calculate_price_estimate() - self.cost_of_goods_sold()
                * (self.calculate_customer_interest() / 100))


with open("resources/apples.json", 'r') as f:
    apple_data = json.load(f)
# opens the file and by using 'with' it auto closes the file after doing the task
# this method helps prevent possible errors from handling the files
print()

print("in this program you will have to calculate which apple has a higher profitability, \n"
      "the way this is done is by doing this formula: \n \n"
      "estimated revenue per apple - cost of goods sold * (customer interest / 100) \n \n"
      "the higher the profitability score the higher the profit. \n")

while True:
    try:
        menu_selection = int(input("1: start program | 2: quit | input number: "))
        if menu_selection == 1:
            print()
            break
        elif menu_selection == 2:
            quit()
        # the reason for the quit option is to prevent a user possibly being stuck
        # in a loop without being able to quit the program
        else:
            print()
            print("please enter either 1 or 2 \n")
    except ValueError:
        print()
        print("please enter either 1 or 2 \n")

question_number = 1
while True:
    print(f"question number {question_number}")
    time.sleep(1.25)
    print()
    Royal_Gala = Apple(**apple_data['Royal_Gala'])
    Granny_Smith = Apple(**apple_data['Granny_Smith'])
    # creates an instance from the apple class for royal gala
    # using ** checks the dictionary for the different attributes.

    Granny_Smith.apple_variance()
    Royal_Gala.apple_variance()
    # these functions change the attribute scores of the apples to make them unique everytime

    if Royal_Gala.profitability_score() > Granny_Smith.profitability_score():
        right_answer = "A"
        right_profitability_score = round(Royal_Gala.profitability_score(), 2)

    elif Granny_Smith.profitability_score() > Royal_Gala.profitability_score():
        right_answer = "B"
        right_profitability_score = round(Granny_Smith.profitability_score(), 2)

    else:
        right_answer = "C"
        right_profitability_score = round(Royal_Gala.profitability_score(), 2)

    print()

    print(f"{Royal_Gala}")
    print(f"Estimated revenue per apple: ${Royal_Gala.calculate_price_estimate():.2f}")
    print("Customer interest:", round((Royal_Gala.calculate_customer_interest()), 2)
          , "out of 100")
    print(f"cost of goods sold: ${Royal_Gala.cost_of_goods_sold():.2f}")
    print(Royal_Gala.profitability_score())
    print()

    print(Granny_Smith)
    print(f"Estimated revenue per apple: ${Granny_Smith.calculate_price_estimate():.2f}")
    print("Customer interest:", round((Granny_Smith.calculate_customer_interest()), 2)
          , "out of 100")
    print(f"cost of goods sold: ${Granny_Smith.cost_of_goods_sold():.2f}")
    print(Granny_Smith.profitability_score())

    print()
    while True:
        try:
            program_selection = int(input("1: answer question | 2: help | input number: "))
            if program_selection == 1:
                break
            # takes the user straight to the answer area.
            elif program_selection == 2:
                print("use the formula provided above to figure out which of the two apples is more profitable. \n"
                      "once you have figured it out, select the apple that has the most profitability \n"
                      "then type in the profitability score you got for it (eg: 0.94 or 1.05).")

                print()

                print("v_quality = visual quality, i_quality = internal quality, s_quality = spoil time")

                print()

                time.sleep(10)
                break
                # the reason I break this code was because once the user has read this they won't need it again.
                # and so taking them to the answer section is the best thing to do.
            else:
                print()
                print("please enter either 1 or 2 \n")
        except ValueError:
            print()
            print("please enter either 1 or 2 \n")
    print()
    while True:
        user_answer = input("A: Royal Gala , B: Granny Smith , or C: Tie | which one is more profitable: ").upper()
        if user_answer == right_answer:
            print("correct answer")
            while True:
                try:
                    user_profitability_score = float(input(f"Enter {right_answer} profitability score "
                                                           f"(rounded to the nearest 2 decimals): "))
                    if user_profitability_score == right_profitability_score:
                        print("correct again, congratulations")
                        time.sleep(2.5)
                        break
                    elif user_profitability_score != right_profitability_score:
                        print(f"wrong answer, right answer was {right_profitability_score}")
                        time.sleep(2.5)
                        break
                except ValueError:
                    print("invalid input")
            break
        elif user_answer not in ["A", "B", "C"]:
            print("invalid input")
        else:
            print(f"wrong answer, right answer was {right_answer}")
            time.sleep(2.5)
            break

    question_number += 1
    terminal_clear()
