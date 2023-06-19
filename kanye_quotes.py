import customtkinter as ctk
from tkinter import *
from PIL import Image
import requests






def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()["quote"]
    
    canvas.itemconfigure(quote_txt,text= data)
    


# ui setup

app = ctk.CTk()
app.title("Kanye says...")
app.config(padx=50, pady=50, bg="#EEEEEE")
app.iconbitmap("icon.ico")
app.resizable(False, False)

canvas = Canvas(width=300, height=414, highlightthickness=0)
bg_img = PhotoImage(file="background.png")
canvas.create_image(150, 207,image = bg_img,)
quote_txt = canvas.create_text(150,207, text="", width=250, font=("Comfortaa", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)


Kanye_img = ctk.CTkImage(light_image= Image.open("kanye.png"), dark_image= Image.open("kanye.png"), size=(100,131))

kanye_btn  = ctk.CTkButton(app, text="", image=Kanye_img, command=get_quote, bg_color="#EEEEEE", hover_color="#FFDE00", fg_color="#EEEEEE")
kanye_btn.grid(row=1, column=0)





app.mainloop()


    




