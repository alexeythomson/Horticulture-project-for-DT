import tkinter

with open("resources/apples.txt", 'r') as file:
    info = file.read()
    print(info)