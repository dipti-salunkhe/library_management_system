import tkinter as tk 
from PIL import Image,ImageTk
window = tk.Tk()
window.title("ksdasndsnadn")


imgpath = '3.jpg'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)


canvas = tk.Canvas(window, bd=5, highlightthickness=100)
canvas.pack()
canvas.create_image(0, 0, image=photo)

window.geometry("1500x1387")

window.mainloop()



