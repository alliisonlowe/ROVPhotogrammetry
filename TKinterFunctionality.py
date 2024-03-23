import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import math

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Application Setup
        self.title("LBCC Photogrammetry Software")
        self.geometry("1280x960")
        self.configure(bg="#333333")

        # Create and add the label to display the image
        self.width, self.height = 1280, 960
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)

        self.pixel_length = 0
        self.ratioLength = 0

        # Create and add the button to upload the image
        self.upload_button = tk.Button(self, text="Locate Image", command=self.image_uploader)
        self.upload_button.grid(row=1, column=0, pady=20)

        # Create and add the button to find pixel size of line
        self.set_button = tk.Button(self, text="Set Line", command=self.find_pixel)
        self.set_button.grid(row=0, column=1, pady=20, padx=10)

        # Create and add the button to set scale for conversion
        self.scale_button = tk.Button(self, text="Create Scale", command=self.set_conversion)
        self.scale_button.grid(row=1, column=1, pady=30, padx=10)

        # Create and add the button to measure coral reef in pixels to convert to cm
        self.convert_button = tk.Button(self, text="Measure Coral Reef", command=self.pixel_to_cm)
        self.convert_button.grid(row=2, column=1, pady=40, padx=10)

        # Create ratio text display on the top left corner
        self.ratio_label = tk.Label(self, text=f"Ratio: {self.ratioLength:.2f} pixels/cm")
        self.ratio_label.grid(row=0, column=2, padx=10, pady=20)

        # Entry widget for user input of length in centimeters
        self.cm_entry = tk.Entry(self)
        self.cm_entry.grid(row=1, column=2, padx=10, pady=20)

        # Add a row and column configuration for the grid
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Creating Points for Drawing a line
        self.points = []
        self.canvas.bind("<Button-1>", self.on_click_disabled)

    def image_uploader(self):
        file_types = [("Image Files", "*.png;*.jpg;*.jpeg")]
        path = filedialog.askopenfilename(filetypes=file_types)

        if len(path):
            self.img = Image.open(path)

            # Define maximum width and height for display
            max_width = 1200
            max_height = 600

            # Calculate scaling factor based on maximum dimensions
            width_ratio = max_width / self.img.width
            height_ratio = max_height / self.img.height
            scaling_factor = min(width_ratio, height_ratio)

            # Resize the image
            new_width = int(self.img.width * scaling_factor)
            new_height = int(self.img.height * scaling_factor)
            self.img = self.img.resize((new_width, new_height))
            self.pic = ImageTk.PhotoImage(self.img)

            # Clear previous image, if any
            self.canvas.delete("image")

            # Display the resized image on the canvas
            self.canvas.create_image(0, 0, image=self.pic, anchor="nw", tag="image")
            self.canvas.config(width=new_width, height=new_height)

    def on_click_disabled(self, event):
        pass

    def on_click(self, event):
        self.points.append((event.x, event.y))

        if len(self.points) == 2:
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]

            self.canvas.create_line(x1, y1, x2, y2, fill="red")
            self.pixel_length = self.calculate_pixel_length(x1, y1, x2, y2)
            print(f"Pixel Length: {self.pixel_length}")

            self.points = []

    def calculate_pixel_length(self, x1, y1, x2, y2):
        pixel_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return pixel_length

    def find_pixel(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<Button-1>", self.on_click)

    def set_conversion(self):
        user_input_cm = self.cm_entry.get()
        try:
            user_input_cm = float(user_input_cm)
            self.ratioLength = self.pixel_length / user_input_cm
            self.ratio_label.config(text=f"Ratio: {self.ratioLength:.2f} pixels/cm")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for centimeters.")

    def pixel_to_cm(self):
        print("THIS IS MY CONVERSION BUTTON")
        # You can implement your conversion logic here

if __name__ == "__main__":
    app = App()
    app.mainloop()