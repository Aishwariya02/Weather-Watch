
from tkinter import *
from tkcalendar import Calendar
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import requests as rq
import random
import webbrowser
import datetime
import time
import json
from PIL import ImageTk, Image
import os
import urllib.request
import datetime as dt


def callback(url):
    webbrowser.open_new(url)


def open_calendar():
    global Cal_window
    Cal_window = Toplevel()
    Cal_window.title("Calender")
    Cal_window.geometry("700x450")
    Cal_window.resizable(0, 0)

    Calendar(Cal_window, font="Ariel 20 bold", borderwidth=10, state="normal").pack()

    def DClock():
        global curr_time
        curr_time = time.strftime("%I:%M:%S")
        clock.config(text=curr_time)
        clock.after(100, DClock)

    message = Label(Cal_window, font=("arial", 100, "italic"), text="Time", fg="red")
    message.place()
    clock = Label(Cal_window, font=("times", 150, "bold"), fg="black")
    clock.place()
    DClock()

    clock = Label(Cal_window, font="courier 15 bold", fg="black", text=DClock())
    clock.pack()

    x = dt.datetime.now()
    global date
    date = x.strftime("%x")
    Label(Cal_window, font="courier 16 bold", fg="black", text=x.strftime("%x")).pack()
    Label(Cal_window, font="courier 15 bold", fg="black", text=x.strftime("%p")).place(x=410, y=338)
    Label(Cal_window, font="courier 16 bold", fg="black", text=x.strftime("%A")).pack()
    Button(Cal_window, text="Enter Notes", font=("Comic Sans MS", 12), command=enter_notes).place(x=10, y=380)
    Button(Cal_window, text="Back", font=("Comic Sans MS", 12), command=delete_Cal_window).place(x=630, y=380)


def open_news():
    global News_window
    News_window = Tk()
    News_window.title("News")
    News_window.geometry("1300x400")
    News_window.resizable(0, 0)

    label_frame = LabelFrame(News_window, text="Current News", width=2, height=5, bd=3, bg="Lightcyan2",
                             font=("Comic Sans MS", 12))
    label_frame.pack()
    n = random.randint(0, 4)
    Label(label_frame, text=news_list[n].title.text, font=("Comic Sans MS bold", 15)).pack()
    link1 = Label(label_frame, text="Click here to know more", fg="blue4", cursor="hand2", font=("Comic Sans MS", 12))
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback(news_list[n].link.text))
    m = random.randint(5, 9)
    Label(label_frame, text=news_list[m].title.text, font=("Comic Sans MS bold", 15)).pack()
    link2 = Label(label_frame, text="Click here to know more", fg="blue4", cursor="hand2", font=("Comic Sans MS", 12))
    link2.pack()
    link2.bind("<Button-1>", lambda e: callback(news_list[m].link.text))
    p = random.randint(10, 14)
    Label(label_frame, text=news_list[p].title.text, font=("Comic Sans MS bold", 15)).pack()
    link3 = Label(label_frame, text="Click here to know more", fg="blue4", cursor="hand2", font=("Comic Sans MS", 12))
    link3.pack()
    link3.bind("<Button-1>", lambda e: callback(news_list[p].link.text))
    r = random.randint(15, 20)
    Label(label_frame, text=news_list[r].title.text, font=("Comic Sans MS bold", 15)).pack()
    link4 = Label(label_frame, text="Click here to know more", fg="blue4", cursor="hand2", font=("Comic Sans MS", 12))
    link4.pack()
    link4.bind("<Button-1>", lambda e: callback(news_list[r].link.text))
    Label(News_window, text=" ", font=("Comic Sans MS bold", 16)).pack()
    Button(News_window, text="Back", font=("Comic Sans MS", 12), command=delete_news_window).pack()


def open_forecast():
    def Weather(win):
        try:
            URL = "https://api.openweathermap.org/data/2.5/weather?q=" + city.get() + "&appid=2185e32c223cff2eb63e4dade103ee95"
            json_data = rq.get(URL).json()
            condition = json_data['weather'][0]['main']
            temp = json_data['main']['temp']
            temprature = int(temp - 273.15)
            min_temp = int(json_data['main']['temp_min'] - 273.15)
            max_temp = int(json_data['main']['temp_max'] - 273.15)
            pressure = int(json_data['main']['pressure'] - 273.15)
            humidity = int(json_data['main']['humidity'] - 273.15)
            print(min_temp)
            print(max_temp)
            print(pressure)
            print(humidity)
            wind = json_data['wind']['speed']
            sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
            sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

            final_info1 = "Condition:  " + condition
            f_i2 = "Temperature:" + str(temprature) + "  C"

            max_t = "Max temp:   " + "\n" + str(max_temp)
            min_t = "Min temp:   " + "\n" + str(min_temp)
            press = "Pressure:" + "\n" + str(pressure)
            hum = "Humidity:" + "\n" + str(humidity)
            win_s = "Wind_speed:" + "\n" + str(wind)
            s_rise = "Sunrise:" + "\n" + str(sunrise) + " am"
            s_set = "Sunset:" + "\n" + str(sunset) + " pm"
            lable1.config(text=final_info1)
            lable2.config(text=f_i2)
            lable3.config(text=max_t)
            minlab.config(text=min_t)
            preelab.config(text=press)
            humlab.config(text=hum)
            winlab.config(text=win_s)
            riselab.config(text=s_rise)
            setlab.config(text=s_set)

        except KeyError:
            global Error_window
            Error_window = Toplevel()
            Error_window.title("City Error")
            Error_window.geometry("250x100")
            Label(Error_window, text="Please enter valid City Name", font=("Comic Sans MS", 12), fg='red').pack()
            Button(Error_window, text="Ok", font=("Comic Sans MS", 12), command=delete_error_window, width=7).pack()

    win = Toplevel()
    win.geometry("1200x660")
    win.title("Weather app")
    f = ("poppins", 12, "bold")
    t = ("poppins", 15, "bold")

    bg_lable = Label(win, image=bg1)
    bg_lable.place(relwidth=1, relheight=1)
    frame = Frame(win, bg='#80c1ff')
    frame.place(x=20, y=100, anchor='n')
    global city
    city = StringVar()

    textfield = Entry(win, font=t, textvariable=city)
    textfield.place(x=180, y=100)
    textfield.focus()
    textfield.bind('<Return>', Weather)

    Label(win, text="City name:", font="comics", fg="black", bg='white').place(x=70, y=100)

    dt = datetime.datetime.now()
    date = Label(win, text=dt.strftime("%A--"), bg='white', font=f)
    date.place(x=650, y=210)

    month = Label(win, text=dt.strftime('%m %B'), bg='white', font=f)
    month.place(x=650, y=240)

    lable3 = Label(win, font=f)
    lable3.place(x=80, y=450)
    lable1 = Label(win, font=f)
    lable1.place(x=450, y=100)
    lable2 = Label(win, font=f)
    lable2.place(x=450, y=130)

    minlab = Label(win, font=f)
    minlab.place(x=240, y=450)
    preelab = Label(win, font=f)
    preelab.place(x=390, y=450)
    humlab = Label(win, font=f)
    humlab.place(x=540, y=450)
    winlab = Label(win, font=f)
    winlab.place(x=690, y=450)
    riselab = Label(win, font=f)
    riselab.place(x=850, y=450)
    setlab = Label(win, font=f)
    setlab.place(x=1050, y=450)


def open_notes():
    global Display
    Display = Tk()
    Display.title("Display Notes")
    Display.geometry("600x450")
    file = open("Notes.txt", 'r')
    content = file.readlines()
    file.close()
    for line in content:
        Label(Display, text=line, font=("Comic Sans MS", 12)).pack()
    Button(Display, text="Back", font=("Comic Sans MS", 12), width=5, command=delete_display).place(x=20, y=400)
    Button(Display, text="Clear Notes", font=("Comic Sans MS", 12), width=12, command=clear_notes).place(x=460, y=400)


def delete_news_window():
    News_window.destroy()


def delete_Cal_window():
    Cal_window.destroy()


def enter_notes():
    global Notes
    Notes = Tk()
    Notes.title("Notes")
    Notes.geometry("400x200")

    global takenotes
    takenotes = StringVar()
    global text

    Label(Notes, text="Enter your Note", font=("Comic Sans MS", 12)).pack()
    text = Entry(Notes, width=30)
    text.pack()
    text.bind('<Return>', store_notes)
    Label(Notes, text=" ", font=("Comic Sans MS", 12)).pack()
    Button(Notes, text="Ok", font=("Comic Sans MS", 10), command=store_notes, width=5).place(x=15, y=150)
    Button(Notes, text="Back", font=("Comic Sans MS", 10), command=delete_notes, width=5).place(x=330, y=150)


def store_notes():
    global notes
    notes = text.get()
    file = open("Notes.txt", 'a')
    file.write(curr_time + "   " + date + "   ")
    file.write(notes + "\n")
    file.close()
    global success
    success = Tk()
    success.title("Note entry success")
    success.geometry("300x150")
    Label(success, text="Note entry success", font=("Comic Sans MS", 12), fg="green").pack()
    Button(success, text="Ok", font=("Comic Sans MS", 10), width=5, command=delete_success).pack()
    text.delete(0, END)


def delete_success():
    success.destroy()


def delete_display():
    Display.destroy()


def clear_notes():
    file = open("Notes.txt", "r")
    erase = file.readlines()
    file.close()
    del erase[0:]

    file = open("Notes.txt", "w+")
    for line in erase:
        file.write(line)
    file.close()

    global notes_clear_window
    notes_clear_window = Tk()
    notes_clear_window.title("Notes Cleared")
    notes_clear_window.geometry("300x100")
    Label(notes_clear_window, text="Notes successfully cleared", font=("Comic Sans MS", 12), fg="green").pack()
    Button(notes_clear_window, text="OK", width=6, font=("Comic Sans MS", 10),
           command=lambda: [delete_notes_clear_window(), delete_display()]).pack()


def delete_notes():
    Notes.destroy()


def delete_notes_clear_window():
    notes_clear_window.destroy()


def Exit():
    main_window.destroy()


global main_window
main_window = Tk()
main_window.title("Main Window")
main_window.geometry("500x420")
main_window.resizable(0, 0)
bg = PhotoImage(file='cartoon-sky.png')
bg_lable = Label(main_window, image=bg)
bg_lable.place(relwidth=1, relheight=1)
Label(main_window, text="What do you want to do?", font=("Comic Sans MS bold", 16)).pack()
Label(main_window, text=" ", font=("Comic Sans MS bold", 16)).pack()
Button(main_window, text="View Calendar", font=("Comic Sans Ms", 12), command=open_calendar).pack()
Label(main_window, text=" ", font=("Comic Sans MS bold", 16)).pack()
Button(main_window, text="View Weather Forecast", font=("Comic Sans MS", 12), command=open_forecast).pack()
Label(main_window, text=" ", font=("Comic Sans MS bold", 16)).pack()
Button(main_window, text="View Current News", font=("Comic Sans MS", 12), command=open_news).pack()
Label(main_window, text=" ", font=("Comic Sans MS bold", 16)).pack()
Button(main_window, text="View Saved Notes", font=("Comic Sans MS", 12), command=open_notes).pack()
Label(main_window, text=" ", font=("Comic Sans MS bold", 16)).pack()
Button(main_window, text="Exit", font=("Comic Sans MS", 12), width=10, command=Exit).pack()

news_url = "https://news.google.com/news/rss"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()

soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")

bg1 = PhotoImage(file='landscape.png')
#bg2=PhotoImage(file='sun2_icon.png')

main_window.mainloop()

