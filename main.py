import json
'''code to compare apple prices '''

class Apple:
    def __init__(self, weight, v_quality, i_quality, s_time):
        self.weight = weight
        self.v_quality = v_quality
        self.i_quality = i_quality
        self.s_time = s_time

with open("resources/apples.json", 'r') as file:
    info = json.load(file)

