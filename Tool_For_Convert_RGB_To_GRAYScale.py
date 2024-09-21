import cv2
import tkinter as tk
from tkinter import filedialog

def convert_images():
    """Converts selected images to grayscale."""
    selected_files = filedialog.askopenfilenames(filetypes=[("Image Files", ".jpg;.png;*.jpeg")])
    for file in selected_files:
        img = cv2.imread(file)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(file.replace(".jpg", "_gray.jpg"), gray_img)  # Replace extension as needed

# Create the GUI window
root = tk.Tk()
root.title("Image Grayscale Converter")

# Create a button to trigger the conversion
convert_button = tk.Button(root, text="Convert Images", command=convert_images)
convert_button.pack()

root.mainloop()