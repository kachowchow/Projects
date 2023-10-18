import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap


def getWeather(city):
      apiKey = "e750d28c77b82d15989655508afdbcee"
      url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
      res = requests.get(url)
      
      if res.status_code == 404:
            messagebox.showerror("Error", "City Not Found")
            return None

      weather = res.json()
      iconNum = weather['weather'][0]['icon']
      temperature = weather['main']['temp'] - 273.15
      description = weather['weather'][0]['description']
      city = weather['name']
      country = weather['sys']['country']

      iconUrl = f"https://openweathermap.org/img/wn/{iconNum}@2x.png"
      return (iconUrl, temperature, description, city, country)



def search():
      city = userInput.get()
      result = getWeather(city)
      if result is None:
            return
      iconUrl, temperature, description, city, country = result
      location.configure(text=f"{city}, {country}")

      image = Image.open(requests.get(iconUrl, stream=True).raw)
      icon = ImageTk.PhotoImage(image)
      iconLabel.confirgure(image=icon)
      iconLabel.image = icon

      temperature.configure(text=f"Temperature: {temperature:.2f}°C")
      description.configure(text=f"Description: {description}")

root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

#create the input field
userInput = ttkbootstrap.Entry(root, font="Calibri , 18")
userInput.pack(pady=10)

searchButton = ttkbootstrap.Button(root, text="Search", command="search", bootstyle="Warning")
searchButton.pack(pady=10)

location = tk.Label(root, font="Calibri, 25")
location.pack(pady=20)

iconLabel = tk.Label(root)
iconLabel.pack()

temperature = tk.Label(root, font="Calibri, 20")
temperature.pack()

description = tk.Label(root, font="Calibri, 20")
description.pack()

root.mainloop()
