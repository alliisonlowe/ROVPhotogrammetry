import tkinter as tk
## Adding Testing Brach

root = tk.Tk()
root.geometry("800x500")
root.title("LBCC ImagePixel-Length Software")

label=tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=30)

textbox =tk.Text(root,height=3, font=('Arial', 16))
textbox.pack()

myentry =tk.Entry(root)
myentry.pack()

root.mainloop()
