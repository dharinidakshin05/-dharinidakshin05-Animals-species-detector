import tkinter as tk
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
class AnimalClassifier:
    def __init__(self, window):
        self.window = window
        self.window.title("Animal Classifier")
        self.image = Image.open(r"C:\Users\shanmugam\Downloads\meow.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(window, image=self.photo)
        self.image_label.pack()
        self.image_label.image = self.photo                
        self.animal_label = tk.Label(window, text="Animal Type:")
        self.animal_label.pack()
        self.animal_entry = tk.Entry(window)
        self.animal_entry.pack()
        self.age_label = tk.Label(window, text="Age category:")
        self.age_label.pack()
        self.age_entry = tk.Entry(window)
        self.age_entry.pack()
        self.button = tk.Button(window, text="Classify", command=self.classify_animal)
        self.button.pack()
        self.classification_label = tk.Label(window, text="")
        self.classification_label.pack()

    def classify_animal(self):
        animal = self.animal_entry.get()
        age = self.age_entry.get()

        if animal.lower() in ["cow", "kangaroo", "elephant","rabbit","deer","horse","invertebrate","zebra"]:
            diet = "Herbivore"
        elif animal.lower() in ["lion", "tiger", "bear","cat","tiger","polar beer","wolf","cheetah","tiger shark"]:
            diet = "Carnivore"
        else:
            diet = "Unknown"

        if age.lower() in ["adult", "mature", "grown-up"]:
            age_group = "Adult"
        elif age.lower() in ["child", "young", "kid"]:
            age_group = "Child"
        else:
            age_group = "Unknown"

        self.classification_label.config(text=f"The {animal} is a {diet} and is a {age_group}.")

window = tk.Tk()
classifier = AnimalClassifier(window)
window.mainloop()
