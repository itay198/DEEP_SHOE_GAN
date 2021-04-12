from tkinter import *
from PIL import ImageTk, Image
import os 
import sys

def Click(labelName):
    if not os.path.isdir(os.path.join(labelName)):
        os.mkdir(labelName)
    global imgLabel
    global notAttributeButton
    global image_number
    global attributeButton
    image_number += 1   
    if image_number == len(images) + 1:
        os.rename(images_paths[image_number-2], os.path.join(os.getcwd(), labelName,images_paths[image_number-2]))
        notAttributeButton.grid_remove()
        notAttributeButton = Button(root,command= lambda: Click(""), text="no more photos",fg="white",bg="black",state="disable")
        notAttributeButton.grid(row="1",column="2")
        attributeButton.grid_remove()
        attributeButton = Button(root,command= lambda: Click(""), text="no more photos",fg="white",bg="black",state="disable")
        attributeButton.grid(row="1",column="0")
        imgLabel.grid_forget()
        return    
    imgLabel.grid_forget()
    imgLabel = Label(image=images[image_number-1])
    imgLabel.grid(row="1",column="1")
    os.rename(images_paths[image_number-2], os.path.join(os.getcwd(), labelName, images_paths[image_number-2]))


if len(sys.argv) != 3:
    exit("add the path to the folder with the images as the first argument\n and add the attribute name as a second arguemnt")

folderPath = sys.argv[1]
attributeName = sys.argv[2]
root = Tk()

images = []
images_paths = []
for filename in os.listdir(folderPath):
    if  not os.path.isdir(os.path.join(folderPath, filename)):
        images.append(ImageTk.PhotoImage(Image.open(os.path.join(folderPath, filename))))
        images_paths.append(filename)
        print(filename)

if len(images) == 0:
    exit("no images found")
imgLabel = Label(image=images[0])
imgLabel.grid(row="1",column="1")
os.chdir(folderPath)

image_number = 1

titleLable = Label(root,text="labeling program - {} or not".format(attributeName))
attributeButton = Button(root,command= lambda: Click("{}".format(attributeName)), text="{}".format(attributeName),fg="white",bg="green")
notAttributeButton = Button(root, command= lambda: Click("not {}".format(attributeName)),text="not {}".format(attributeName),fg="white",bg="red")

titleLable.grid(row="0", column="1")
attributeButton.grid(row="1",column="0")
notAttributeButton.grid(row="1",column="2")

root.mainloop()

