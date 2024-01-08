from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize the Tkinter window
root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

# Function to calculate BMI and display result
def BMI():
    h = float(Height.get())
    w = float(Weight.get())
    m = h / 100
    bmi = round(float(w / m ** 2), 1)
    label1.config(text=bmi)

    if bmi <= 18.5:
        label2.config(text="This is Underweight!")
        label3.config(text="You have lower weight than normal body!")
    elif bmi > 18.5 and bmi <= 25:
        label2.config(text="This is Normal!")
        label3.config(text="You have what is referred to as normal body weight!")
    elif bmi > 25 and bmi <= 30:
        label2.config(text="Overweight!")
        label3.config(text="You have higher weight than normal body!")
    else:
        label2.config(text="Obese!")
        label3.config(text="You have higher weight than overweighted people!")

# Set icon for the window
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# Display top image
top = PhotoImage(file="top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-1, y=-10)

# Display a bottom box
Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

# Display two boxes
box = PhotoImage(file="box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

# Display a scale image
scale = PhotoImage(file="scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=310)

# Create a slider for height input
current_value = tk.DoubleVar()

# Function to get current value from slider
def get_current_value():
    return '{: .2f}'.format(current_value.get())

# Function to handle slider change
def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = Image.open("man.png")
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550 - size)
    secondimage.image = photo2

style = ttk.Style()
style.configure("Tscale", background='white')
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style='TScale', command=slider_changed,
                   variable=current_value)
slider.place(x=80, y=250)

# Create a slider for weight input
current_value2 = tk.DoubleVar()

# Function to get current value from weight slider
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

# Function to handle weight slider change
def slider_changed2(event):
    Weight.set(get_current_value2())

style2 = ttk.Style()
style2.configure("Tscale", background='white')
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style='TScale', command=slider_changed2,
                    variable=current_value2)
slider2.place(x=300, y=250)

# Entry boxes for height and weight
Height = StringVar()
Weight = StringVar()

height = Entry(root, textvariable=Height, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font='arial 50', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())

# Display the man image
secondimage = Label(root, bg='lightblue')
secondimage.place(x=70, y=530)

# Button to calculate BMI
Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", command=BMI).place(x=280,
                                                                                                            y=340)

# Labels to display BMI result and interpretation
label1 = Label(root, font="arial 60 bold", bg="lightblue", fg="#fff")
label1.place(x=125, y=305)

label2 = Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=280, y=430)

label3 = Label(root, font="arial 10", bg="lightblue")
label3.place(x=200, y=500)

root.mainloop()
