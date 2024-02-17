import cv2
import easygui
import numpy as np
import imageio
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Button  # Added imports for Label and Button
from PIL import ImageTk, Image

def cartoonify(ImagePath):
    # Read the image
    original_image = cv2.imread(ImagePath)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    
    # Confirm that the image is chosen
    if original_image is None:
        print("Cannot find any image. Choose appropriate file.")
        sys.exit()

    # Convert image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
    
    # Apply median blur to smooth the image
    smooth_image = cv2.medianBlur(gray_image, 7)  # Increase kernel size for more smoothing
    
    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(smooth_image, 255, 
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)
    
    # Apply bilateral filter to reduce noise while keeping edges sharp
    color_image = cv2.bilateralFilter(original_image, 9, 300, 300)  # Adjust parameters as needed
    
    # Combine the edges with the original image using bitwise_and
    cartoon_image = cv2.bitwise_and(color_image, color_image, mask=edges)
    
    # Display the result
    plt.figure(figsize=(8, 6))
    plt.imshow(cartoon_image)
    plt.axis('off')
    plt.show()

def upload():
    ImagePath=easygui.fileopenbox()
    cartoonify(ImagePath)

top=tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='white')
label = tk.Label(top,background='#CDCDCD', font=('calibri',20,'bold'))  # Changed Label to tk.Label

upload = tk.Button(top,text="Cartoonify an Image",command=upload,padx=10,pady=5)  # Changed Button to tk.Button
upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
upload.pack(side=tk.TOP,pady=50)  # Changed TOP to tk.TOP

top.mainloop()
