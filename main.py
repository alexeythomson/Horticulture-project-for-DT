import json
'''code to show profitability '''

class Apple:
    def __init__(self, name, weight, v_quality, i_quality, s_time):
        self.name = name
        self.weight = weight
        self.v_quality = v_quality
        self.i_quality = i_quality
        self.s_time = s_time

    def __repr__(self):
        return f"{self.name}, {self.weight} grams, {self.v_quality}, {self.i_quality}, {self.s_time}"

with open("resources/apples.json", 'r') as f:
    apple_attributes = json.load(f)


Royal_Gala = Apple(**apple_attributes['Royal_gala'])

print(Royal_Gala)