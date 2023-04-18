from tkinter import *
from PIL import Image, ImageTk
import os
import random

def get_image_male_short():
    directory = "C:/Users/Asus/Desktop/Images/MS" 
    image_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_list.append(os.path.join(directory, filename))
    return image_list

def get_image_male_medium():
    directory = "C:/Users/Asus/Desktop/Images/MM" 
    image_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_list.append(os.path.join(directory, filename))
    return image_list

def get_image_male_tall():
    directory = "C:/Users/Asus/Desktop/Images/MT" 
    image_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_list.append(os.path.join(directory, filename))
    return image_list


def get_image_female_short():
    directory = "C:/Users/Asus/Desktop/Images/FS" 
    image_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_list.append(os.path.join(directory, filename))
    return image_list


def get_image_female_medium():
    directory = "C:/Users/Asus/Desktop/Images/FM" 
    image_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_list.append(os.path.join(directory, filename))
    return image_list


def get_image_female_tall():
    directory = "C:/Users/Asus/Desktop/Images/FT" 
    image_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_list.append(os.path.join(directory, filename))
    return image_list



def main():
    root = Tk()
    root.geometry("500x500")

    image_list = []

    gender = input("Please enter gender: ") 
    height = float(input("Please enter height: "))

    if (gender == "male" or gender == "Male") and height < 5.0:
        image_list = get_image_male_short()
    elif (gender == "male" or gender == "Male") and height >5.0 and height <5.9:
        image_list = get_image_male_medium()
    elif (gender == "male" or gender == "Male") and height > 5.9:
        image_list = get_image_male_tall()
    elif (gender == "female" or gender =="Female") and height < 5.2:
        image_list = get_image_female_short()
    elif (gender == "female" or gender == "Female") and height >=5.2 and height <= 5.7:
        image_list = get_image_female_medium()
    elif (gender == "female" or gender == "Female") and height > 5.7:
        image_list = get_image_female_tall()
    else:
        print("Wrong Choice")
    random_image = random.choice(image_list)

    image = Image.open(random_image)
    resized_image = image.resize((500, 500))
    img = ImageTk.PhotoImage(resized_image)
    panel = Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")

    

    root.mainloop()

if __name__ == '__main__':
    main()
