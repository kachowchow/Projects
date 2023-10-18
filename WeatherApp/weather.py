import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

import config


def getWeather(city):

      


def search():
      city = userInput.get()
      result = getWeather(city)
      if result is None:
            return


root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400 x 400")

#create the input field
userInput = ttkbootstrap.Entry(root, font="Calibri , 18")
userInput.pack(pady=10)

searchButton = ttkbootstrap.Button(root, text="Search", command="search", bootstyle="Warning")
searchButton.pack(pady=10)

location = tk.Label(root, font="Calibri, 25")
location.pack(pady=20)

icon = tk.Label(root)
icon.pack()

temperature = tk.Label(root, font="Calibri, 20")
temperature.pack()

description = tk.Label(root, font="Calibri, 20")
description.pack()

root.mainloop()
#output the location on the window



#Show the weather image



#Output temperature and description