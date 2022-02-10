from tkinter import*
import time
import requests
from tkinter import messagebox
from PIL import ImageTk,Image
from datetime import datetime

#-------------------------App----------------------------------------
app = Tk()
app.title("Weather App")
#app.iconbitmap(r'icon.ico') #iconApp
app.geometry('400x720')
bc = background='#CCFFFF' #FFE4E1,#CCFFFF
app.configure(background=bc)

#-------------------------fonts-------------------------------------
f1 = font= ("poppins",20,"bold")
f2 = font= ("poppins",10,"bold")
f3 = font= ("poppins",12,"bold")
f4 = font= ("poppins",15,"bold")


def get_weather(city):
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    result = requests.get(api)
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_celsius = float("{:.2f}".format(json['main']['temp'] - 273.15))
        min_temp = float("{:.2f}".format(json['main']['temp_min'] - 273.15))
        max_temp = float("{:.2f}".format(json['main']['temp_max'] - 273.15))
        pressure = float("{:.2f}".format(json['main']['pressure']))
        humidity = float("{:.2f}".format(json['main']['humidity']))
        wind = float("{:.2f}".format(json['wind']['speed']))
        sunrise = time.strftime('%I:%M', time.gmtime(json['sys']['sunrise'] -18000))
        sunset = time.strftime('%I:%M', time.gmtime(json['sys']['sunset'] -18000))
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city,country,temp_celsius,min_temp,max_temp,pressure,humidity,wind,sunrise,sunset,icon,weather)
        return final
    else: return None

def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        date_Today()
        location_lbl['text']='{}, {}'.format(weather[0],weather[1])
        temp_lbl['text']='{} °C'.format(weather[2])
        weather_lbl['text']='{}'.format(weather[11])
        maxmin_lbl['text']='Max {} °C Min {} °C'.format(weather[4], weather[3])
        pressure_lbl['text']='{} hPa\nPressure'.format(weather[5])
        humidity_lbl['text'] = '{} %\nHumidity'.format(weather[6])
        wind_lbl['text'] = '{}\nWind'.format(weather[7])
        sunrise_lbl['text'] = '{} AM'.format(weather[8])
        sunset_lbl['text'] = '{} PM'.format(weather[9])
        global icon
        icon =ImageTk.PhotoImage(Image.open('weather_ic\{}.png'.format(weather[10])))
        imagicon_lbl.config(image=icon)
    else: messagebox.showerror('Error','Cannot find city {}'.format(city))

def get_weatherF(city):
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    result = requests.get(api)
    if result :
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_Fahrenheit = float("{:.2f}".format((json['main']['temp'] - 273.15)*(9/5) +32))
        min_temp = float("{:.2f}".format((json['main']['temp_min'] - 273.15)*(9/5) +32))
        max_temp = float("{:.2f}".format((json['main']['temp_max'] - 273.15)*(9/5) +32))
        pressure = float("{:.2f}".format(json['main']['pressure']))
        humidity = float("{:.2f}".format(json['main']['humidity']))
        wind = float("{:.2f}".format(json['wind']['speed']))
        sunrise = time.strftime('%I:%M', time.gmtime(json['sys']['sunrise'] -18000))
        sunset = time.strftime('%I:%M', time.gmtime(json['sys']['sunset'] -18000))
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city,country,temp_Fahrenheit,min_temp,max_temp,pressure,humidity,wind,sunrise,sunset,icon,weather)
        return final
    else: return None

def search_F():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        date_Today()
        location_lbl['text']='{}, {}'.format(weather[0],weather[1])
        temp_lbl['text']='{} °F'.format(weather[2])
        weather_lbl['text']='{}'.format(weather[11])
        maxmin_lbl['text']='Max {} °F Min {} °F'.format(weather[4], weather[3])
        pressure_lbl['text']='{} hPa\nPressure'.format(weather[5])
        humidity_lbl['text'] = '{} %\nHumidity'.format(weather[6])
        wind_lbl['text'] = '{}\nWind'.format(weather[7])
        sunrise_lbl['text'] = '{} AM'.format(weather[8])
        sunset_lbl['text'] = '{} PM'.format(weather[9])
        global icon
        icon =ImageTk.PhotoImage(Image.open('weather_ic\{}.png'.format(weather[10])))
        imagicon_lbl.config(image=icon)
    else: messagebox.showerror('Error','Cannot find city {}'.format(city))

#---------------------------------------------------------------------------------------

def date_Today():
        now = datetime.today()
        date_lbl =Label(app,text=now.strftime("%d/%m/%Y %H:%M"), font=f2,bg=bc)
        date_lbl.place(x=150,y=250)
#------------------------IMG_App------------------------------------
Appname_lbl = ImageTk.PhotoImage(Image.open('appname.png'))
Apppanel = Label(app,image=Appname_lbl,background=bc)
Apppanel.pack(pady=10)


#-----------------Img_Sun---------------------
imgsun = ImageTk.PhotoImage(Image.open('sun.png'))
imgsun_lbl = Label(app,image=imgsun,background=bc)
imgsun_lbl.place(x=0,y=450)

#------------------------------ช่องค้นหา-------------------------------
city_text= StringVar()
city_entry = Entry(app, textvariable= city_text,width = 30,font=f4)
city_entry.pack(pady=10)

#------------------------------Button---------------------------------
search_btn = Button(app,text='Search City', font= ("poppins",10,"bold"),width = 20, command= search,bg='black',fg='white')
search_btn.pack()

searchF_btn = Button(app,text='F', font= ("poppins",10,"bold"),width = 3, command= search_F,bg=bc,fg='black')
searchF_btn.place(x=300,y=222)

searchC_btn = Button(app,text='C', font= ("poppins",10,"bold"),width = 3, command= search,bg=bc,fg='black')
searchC_btn.place(x=335,y=222)
#-------------------------------Location------------------------------
location_lbl = Label(app, text='', font= ("poppins",25,"bold"),bg=bc)
location_lbl.pack(pady=10)

#----------------Icons-----------------
imagicon_lbl = Label(app, image='',bg=bc)
imagicon_lbl.pack()

#---------------------Weather-----------------------------------------
weather_lbl = Label(app, text='',font= f1,bg=bc)
weather_lbl.pack()

#-----------------------------Temp------------------------------------
temp_lbl = Label(app, text='',font= f4,bg=bc)
temp_lbl.pack()

#--------------------------Max-Min------------------------------------
maxmin_lbl = Label(app, text='',font=f3,bg=bc)
maxmin_lbl.pack()

#------------------------------Pressure-------------------------------
pressure_lbl = Label(app, text='-\nPressure',font= f2,bg=bc)
pressure_lbl.place(x=300,y=670)

#-------------------------Humidity------------------------------------
humidity_lbl = Label(app, text='-\nHumidity',font= f2,bg=bc)
humidity_lbl.place(x=190,y=670)

#-----------------------------Wind------------------------------------
wind_lbl = Label(app, text='-\nWind',font= f2,bg=bc)
wind_lbl.place(x=70,y=670)

#------------------------------Sun-----------------------------------------
sunrise_lbl = Label(app, text='',font= f2,bg=bc)
sunrise_lbl.place(x=15,y=620)

sunset_lbl = Label(app, text='',font= f2,bg=bc)
sunset_lbl.place(x=325,y=620)


app.mainloop()

