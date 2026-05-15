"""
Program to make the end user work out the profitability of an apple by using a formula provided to them,
and then they will have to figure out which apple is more profitable.
"""
import json
import random
import time

PRICE_ESTIMATE_DIVIDER = 250
APPLE_SCORE_DIVIDER = 1.25
APPLE_SCORE_MULTIPLICATION = 12.5
CUSTOMER_INTEREST_DIVIDER = 15
CUSTOMER_INTEREST_MULTIPLICATION = 1.8
PROFITABILITY_SCORE_DIVIDER = 100

# these prevent literals in my code


def terminal_clear():
    """this clears the space between each question and prevents
    a pile up which can be annoying for the end user."""
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
        This will make every interaction different from the last which makes it good
        for the end user. I use min to make sure the attributes
        don't go over the maximum which is 10 as well as the max for weight to prevent it
        from going into the negatives."""
        self.v_quality = min(10, self.v_quality + random.uniform(-1.5, 4))
        self.i_quality = min(10, self.i_quality + random.uniform(-1.5, 4))
        self.s_time = min(10, self.s_time + random.uniform(-1.5, 4))
        self.weight = round(max(0, min(300, self.weight * random.uniform(0.9, 1.15))), 1)

    def calculate_apple_score(self):
        """this calculates a score for the apple which the price estimate and consumer interest
        calculations will work off of, this helps reduce unnecessary code"""

        return (self.weight / APPLE_SCORE_DIVIDER) + ((self.v_quality + self.i_quality + self.s_time)
                                                      * APPLE_SCORE_MULTIPLICATION)

    def calculate_price_estimate(self):
        """calculates the estimated revenue per apple using the apple score."""
        apple_score = self.calculate_apple_score()
        return apple_score / PRICE_ESTIMATE_DIVIDER

    def calculate_customer_interest(self):
        """Calculates the customer interest on an apple by using the apple score together with
        a multiple that will increase depending on certain attributes.
        For this code I add in a min(100, score) which basically returns whatever is lower, the calculated score
        or if the scores over 100, the code returns 100. This prevents it from going over the max"""

        apple_score = self.calculate_apple_score()
        score = (apple_score / CUSTOMER_INTEREST_DIVIDER) + (self.v_quality + self.i_quality
                                                             + self.s_time) * CUSTOMER_INTEREST_MULTIPLICATION
        return min(100, score)

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
                * (self.calculate_customer_interest() / PROFITABILITY_SCORE_DIVIDER))


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
    royal_gala = Apple(**apple_data['Royal_Gala'])
    granny_smith = Apple(**apple_data['Granny_Smith'])
    # creates an instance from the apple class for royal gala
    # using ** checks the dictionary for the different attributes.

    granny_smith.apple_variance()
    royal_gala.apple_variance()
    # these functions change the attribute scores of the apples to make them unique everytime

    if royal_gala.profitability_score() > granny_smith.profitability_score():
        right_answer = "A"
        right_profitability_score = round(royal_gala.profitability_score(), 2)

    elif granny_smith.profitability_score() > royal_gala.profitability_score():
        right_answer = "B"
        right_profitability_score = round(granny_smith.profitability_score(), 2)

    else:
        right_answer = "C"
        right_profitability_score = round(royal_gala.profitability_score(), 2)
    print()

    print(f"{royal_gala}")
    print(f"Estimated revenue per apple: ${royal_gala.calculate_price_estimate():.2f}")
    print("Customer interest:", round((royal_gala.calculate_customer_interest()), 2)
          , "out of 100")
    print(f"cost of goods sold: ${royal_gala.cost_of_goods_sold():.2f}")

    print()

    print(granny_smith)
    print(f"Estimated revenue per apple: ${granny_smith.calculate_price_estimate():.2f}")
    print("Customer interest:", round((granny_smith.calculate_customer_interest()), 2)
          , "out of 100")
    print(f"cost of goods sold: ${granny_smith.cost_of_goods_sold():.2f}")

    print()
    while True:
        try:
            program_selection = int(input("1: answer question | 2: help | 3: quit | input number: "))
            if program_selection == 1:
                break
            # takes the user straight to the answer area.
            elif program_selection == 3:
                quit()
            # another quit for when the user wants to stop the program
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
                print("please enter either 1, 2, or 3 \n")
        except ValueError:
            print()
            print("please enter either 1, 2, or 3 \n")
    print()
    while True:
        user_answer = input("A: Royal Gala , B: Granny Smith , or C: Tie | which one is more profitable: ").upper()
        if user_answer == right_answer:
            print("correct answer")
            while True:
                try:
                    user_profitability_score = float(input(f"Enter {right_answer} profitability score "
                                                           f"(rounded to the nearest 2 decimals): "))
                    if abs(user_profitability_score - right_profitability_score) <= 0.02:
                        print("correct again, congratulations")
                        time.sleep(2.5)
                        break
                    else:
                        print(f"wrong answer, right answer was {right_profitability_score}")
                        time.sleep(2.5)
                        break
                except ValueError:
                    print("invalid input")
            break
            # this break takes the code out of an endless answer cycle
        elif user_answer not in ["A", "B", "C"]:
            print("invalid input")
        else:
            print(f"wrong answer, right answer was {right_answer}")
            time.sleep(2.5)
            break

    question_number += 1
    terminal_clear()
