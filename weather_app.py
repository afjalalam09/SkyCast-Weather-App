from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    
    api_key = "YOUR_API_KEY_HERE"
    
    try:
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").json()
        
        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"].title())
        # Appended units to Temperature and Pressure data
        temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)) + " °C")
        per_label1.config(text=str(data["main"]["pressure"]) + " hPa")
    except Exception as e:
        # Prevents application crash in case of network issues or invalid data
        w_label1.config(text="Error")
        wb_label1.config(text="Data not found")
        temp_label1.config(text="-")
        per_label1.config(text="-")

win = Tk()
win.title("SkyCast - Real-Time Weather")
win.config(bg="#87CEEB") # Soft Sky Blue background
win.geometry("500x570")

# Main Heading Label
name_label = Label(win, text="SkyCast Weather",
                   font=("Helvetica", 30, "bold"), bg="white", fg="#2C3E50")
name_label.place(x=25, y=50, height=50, width=440)

# List of states & cities
city_name = StringVar()
list_name = ("Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh",
             "Chhattisgarh", "Dadra and Nagar Haveli", "Daman and Diu",
             "National Capital Territory of Delhi", "Goa", "Gujarat",
             "Haryana", "Himachal Pradesh", "Jaipur", "Jammu and Kashmir",
             "Jharkhand", "Karnataka", "Kerala", "Lakshadweep", "Madhya Pradesh",
             "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha",
             "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
             "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
             "Andaman and Nicobar Islands")

# Combobox (Dropdown)
com = ttk.Combobox(win, values=list_name, font=("Helvetica", 15), textvariable=city_name)
com.place(x=25, y=120, height=50, width=430)
com.set("Select State / City") # Default placeholder text for the dropdown

# Weather Climate
w_label = Label(win, text="Climate", font=("Helvetica", 18, "bold"), bg="#87CEEB", fg="#2C3E50", anchor="w")
w_label.place(x=25, y=260, height=50, width=200)
w_label1 = Label(win, text="", font=("Helvetica", 18), bg="white", fg="#2C3E50")
w_label1.place(x=230, y=260, height=50, width=235)

# Weather Description
wb_label = Label(win, text="Description", font=("Helvetica", 18, "bold"), bg="#87CEEB", fg="#2C3E50", anchor="w")
wb_label.place(x=25, y=330, height=50, width=200)
wb_label1 = Label(win, text="", font=("Helvetica", 18), bg="white", fg="#2C3E50")
wb_label1.place(x=230, y=330, height=50, width=235)

# Temperature
temp_label = Label(win, text="Temperature", font=("Helvetica", 18, "bold"), bg="#87CEEB", fg="#2C3E50", anchor="w")
temp_label.place(x=25, y=400, height=50, width=200)
temp_label1 = Label(win, text="", font=("Helvetica", 18), bg="white", fg="#2C3E50")
temp_label1.place(x=230, y=400, height=50, width=235)

# Pressure
per_label = Label(win, text="Pressure", font=("Helvetica", 18, "bold"), bg="#87CEEB", fg="#2C3E50", anchor="w")
per_label.place(x=25, y=470, height=50, width=200)
per_label1 = Label(win, text="", font=("Helvetica", 18), bg="white", fg="#2C3E50")
per_label1.place(x=230, y=470, height=50, width=235)

# Done Button
done_button = Button(win, text="Get Weather", font=("Helvetica", 16, "bold"), 
                     bg="#2C3E50", fg="white", command=data_get, cursor="hand2")
done_button.place(y=190, height=50, width=160, x=170)

win.mainloop()