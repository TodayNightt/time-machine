#!/usr/bin/env python

# External imports
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import datetime

# Local imports
from common.api.time_machine import On_this_day
import common.dbs.history as history
from config import API_KEY, ASSETS_DIR

# Define all the Initial variables
clicked = False
this_day, this_month, this_year, date = '', '', '', ''
data = ''

day_drop = []
for i in range(1, 32):
    number = str(i).zfill(2)
    day_drop.append(number)
month_drop = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
              'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
year_drop = list(sorted(range(1500, 2023), reverse=True))


# Functions
def update():
    # Update the day img
    img_d1 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_day[0]}.jpg'))
    img_d2 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_day[1]}.jpg'))
    label_d1.config(image=img_d1)
    label_d1.image_names = img_d1
    label_d2.config(image=img_d2)
    label_d2.image_names = img_d2

    # Update the month img
    img_m1 = ImageTk.PhotoImage(
        Image.open(f'{ASSETS_DIR}/date_img/{this_month[0]}.jpg'))
    img_m2 = ImageTk.PhotoImage(
        Image.open(f'{ASSETS_DIR}/date_img/{this_month[1]}.jpg'))
    label_m1.config(image=img_m1)
    label_m1.image_names = img_m1
    label_m2.config(image=img_m2)
    label_m2.image_names = img_m2

    # Update the year img
    img_y1 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_year[0]}.jpg'))
    img_y2 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_year[1]}.jpg'))
    img_y3 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_year[2]}.jpg'))
    img_y4 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_year[3]}.jpg'))
    label_y1.config(image=img_y1)
    label_y1.image_names = img_y1
    label_y2.config(image=img_y2)
    label_y2.image_names = img_y2
    label_y3.config(image=img_y3)
    label_y3.image_names = img_y3
    label_y4.config(image=img_y4)
    label_y4.image_names = img_y4

    # Check whether got things in the textbox, if yes then delete it for inserting other text
    if len(text_births.get("1.0", "end-1c")) != 0:
        text_births.config(state='normal')
        text_births.delete(1.0, 'end')
        text_death.config(state='normal')
        text_death.delete(1.0, 'end')
        text_events.config(state='normal')
        text_events.delete(1.0, 'end')


# Collects value for the On this day api when OK is pressed
def getData():
    global clicked
    global this_day, this_month, this_year
    this_day = clicked_day.get()
    month_alpha = clicked_months.get()
    this_year = clicked_year.get()
    # If nothing had been selected, it will show a error
    if (this_day == 'Day' or month_alpha == 'Months' or this_year == 'Year'):
        label_error.grid(row=4, column=0, columnspan=3)

    else:
        clicked = True
        label_transfer.grid(row=0, column=0, columnspan=4)
        label_error.destroy()
        this_month = month_drop[month_alpha]
        update()
        global data
        date = f'{this_month}/{this_day}'
        data = On_this_day(date, int(this_year))
        data.getData()
        text_births.insert(INSERT, data.getBirths())
        text_births.config(state="disable")
        text_death.insert(INSERT, data.getDeaths())
        text_death.config(state="disable")
        text_events.insert(INSERT, data.getEvents())
        text_events.config(state="disable")
        text_holidays.insert(INSERT, data.getHolidays())
        text_holidays.config(state="disable")
        data.exportDatabase()
        history.writeHistory()


# Shows the search history


def history_win():
    history_win = Tk()
    history_win.geometry('400x500')
    history_win.config(background='#2BA4B8')
    history_win.minsize(400, 500)
    history_win.maxsize(400, 500)
    history_win.config(padx=10, pady=10)
    history_win.title('History')
    history_win.iconbitmap('assets/icon/parchment.ico')

    order = ['Date', 'Birth', 'Death', 'Event', 'Holiday']
    text_history = Text(history_win, font=(
        'Poppins', 10, 'bold'), padx=10, height=20, width=45)
    text = history.exportJson()
    for items in text:
        for i, item in enumerate(items):
            if i == 0:
                text_history.insert(INSERT, item)
            else:
                text_history.insert(INSERT, '\n' + order[i] + '\n')
                if item[0] != 'No result found':
                    for line in item:
                        text_history.insert(
                            INSERT, line['name'] + '\n' + line['urls'] + '\n')
                else:
                    text_history.insert(INSERT, item[0] + '\n\n')

    copyright_text = '''History icons created by Freepik - Flaticon    https://www.flaticon.com/free-icons/history'''
    text_history.grid(row=0, column=0, columnspan=3)
    Label(
        history_win, text=copyright_text, pady=5, font=('Poppins', 6, 'bold'), background='#2BA4B8').grid(row=1,
                                                                                                          column=0,
                                                                                                          sticky=W)


def quit():
    # Delete all the search history before quiting the window
    history.deleteHistory()
    root.quit()


if __name__ == "__main__":
    if (API_KEY is None or ASSETS_DIR is None):
        print("API_KEY and ASSETS_DIR env need to be set!")
        exit(1)
    # Checks whether today's date is needed when first opening the window
    if not clicked:
        today_date = list(str(datetime.date.today()))
        for i in range(0, 4):
            this_year = this_year + today_date[i]
        for i in range(5, 7):
            this_month = this_month + today_date[i]
        for i in range(8, 10):
            this_day = this_day + today_date[i]

    # GUI
    # Create window
    root = Tk()
    root.geometry('730x755')
    root.config(background='#2BA4B8')
    root.minsize(730, 810)
    root.maxsize(730, 910)
    root.iconbitmap(f'{ASSETS_DIR}/icon/time-machine.ico')
    root.title('Time Machine')
    Label(
        root, text='''Scifi icons created by Freepik - Flaticon      https: // www.flaticon.com/free-icons/scifi''',
        background='#2BA4B8', font=('Poppins', 6, 'bold')).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Dropmenu variables
    clicked_day = StringVar()
    clicked_day.set('Day')
    clicked_months = StringVar()
    clicked_months.set('Months')
    clicked_year = StringVar()
    clicked_year.set('Year')

    # Create canvas for input
    canvas_input = Canvas(root, width=500, height=30, highlightthickness=0)
    canvas_input.grid(row=0, column=0, columnspan=50,
                      padx=20, pady=5, sticky=W)

    # Create calender
    frame_calender = Frame(canvas_input, width=400, height=200, padx=5)
    frame_calender.grid(row=0, column=0, columnspan=3, padx=20)

    # Default today's image
    image_d1 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_day[0]}.jpg'))
    image_d2 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_day[1]}.jpg'))
    image_m1 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_month[0]}.jpg'))
    image_m2 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_month[1]}.jpg'))
    image_y1 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_year[0]}.jpg'))
    image_y2 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_year[1]}.jpg'))
    image_y3 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_year[2]}.jpg'))
    image_y4 = ImageTk.PhotoImage(Image.open(
        f'{ASSETS_DIR}/date_img/{this_year[3]}.jpg'))

    spacer_3 = Label(frame_calender, text="",
                     font=('Poppins', 15, 'bold'), pady=5)
    label_transfer = Label(
        frame_calender, text='Traveling to ~~', font=('Poppins', 15, 'bold'), pady=5)

    label_calender_day = Label(frame_calender, text='Day',
                               font=('Poppins', 15, 'bold'))
    label_d1 = Label(frame_calender, image=image_d1)
    label_d2 = Label(frame_calender, image=image_d2)
    spacer_1 = Label(frame_calender, text="  ")

    label_calender_month = Label(
        frame_calender, text='Month', font=('Poppins', 15, 'bold'))
    label_m1 = Label(frame_calender, image=image_m1)
    label_m2 = Label(frame_calender, image=image_m2)
    spacer_2 = Label(frame_calender, text="  ")

    label_calender_year = Label(
        frame_calender, text='Year', font=('Poppins', 15, 'bold'))
    label_y1 = Label(frame_calender, image=image_y1)
    label_y2 = Label(frame_calender, image=image_y2)
    label_y3 = Label(frame_calender, image=image_y3)
    label_y4 = Label(frame_calender, image=image_y4)
    spacer_4 = Label(frame_calender, text="", font=('Poppins', 15, 'bold'))

    spacer_3.grid(row=0, column=0)
    label_calender_day.grid(row=1, column=0, columnspan=2)
    label_d1.grid(row=2, column=0)
    label_d2.grid(row=2, column=1)
    spacer_1.grid(row=2, column=2)
    label_calender_month.grid(row=1, column=3, columnspan=2)
    label_m1.grid(row=2, column=3)
    label_m2.grid(row=2, column=4)
    spacer_2.grid(row=2, column=5)
    label_calender_year.grid(row=1, column=6, columnspan=4)
    label_y1.grid(row=2, column=6)
    label_y2.grid(row=2, column=7)
    label_y3.grid(row=2, column=8)
    label_y4.grid(row=2, column=9)
    spacer_4.grid(row=3, column=0)

    # Create Input
    frame_input = Frame(canvas_input, width=100, height=150,
                        padx=10, pady=20, background='#ED8C4E')
    label_date = Label(frame_input, text='Select a date',
                       background='#49474E', foreground='white', font=('Poppins', 9, 'bold'))
    label_year = Label(frame_input, text='Select a year',
                       background='#49474E', foreground='white', font=('Poppins', 9, 'bold'))
    drop_day = ttk.Combobox(
        frame_input, textvariable=clicked_day, values=day_drop, background='#D2C6B8')
    drop_month = ttk.Combobox(
        frame_input, textvariable=clicked_months, values=[item for item in month_drop.keys()])
    drop_year = ttk.Combobox(
        frame_input, textvariable=clicked_year, values=year_drop)
    drop_day.config(width=5, justify=CENTER)
    drop_month.config(width=10, justify=CENTER)
    drop_year.config(width=8)

    Label(frame_input, text='',
          foreground='#C73E1D', background='#ED8C4E', font=('Poppins', 10, 'bold')).grid(row=4, column=0, columnspan=2)
    label_error = Label(
        frame_input, text='Please select a value', foreground='#C73E1D', background='#ED8C4E', font=('Poppins', 10, 'bold'))

    button_ok = Button(frame_input, text='OK', command=getData,
                       background='black', foreground='white')
    button_quit = Button(frame_input, text='Quit',
                         command=quit, background='black', foreground='white')
    button_history = Button(frame_input, text='History',
                            foreground='white', background='black', command=history_win)

    frame_input.grid(row=0, column=6)
    label_date.grid(row=0, column=0)
    drop_day.grid(row=1, column=0, pady=5)
    drop_month.grid(row=1, column=1, columnspan=2)
    label_year.grid(row=2, column=0)
    drop_year.grid(row=3, column=0, columnspan=3, pady=5)
    button_ok.grid(row=5, column=0, padx=0)
    button_quit.grid(row=5, column=1, padx=1)
    button_history.grid(row=5, column=2, padx=1)

    # Create output
    canvas_output = Canvas(root, width=500, height=30,
                           highlightthickness=0)
    canvas_output.grid(row=1, column=0, columnspan=50, padx=20)

    # Births
    frame_births = Frame(canvas_output, width=100, height=200, padx=5, pady=5)
    frame_births.grid(row=0, column=0, columnspan=3, padx=20, sticky=W)

    label_births_text = Label(frame_births, text='Births',
                              font=('Poppins', 13))
    text_births = Text(frame_births, wrap=WORD, font=(
        'Poppins', 10), width=80, height=5)

    label_births_text.grid(row=0, column=0, columnspan=2, sticky=W)
    text_births.grid(row=1, column=0)

    # Deaths
    frame_death = Frame(canvas_output, width=50, height=200, padx=5, pady=5)
    frame_death.grid(row=1, column=0, columnspan=3, padx=20)

    label_death_text = Label(frame_death, text='Deaths',
                             font=('Poppins', 13))
    text_death = Text(frame_death, wrap=WORD, font=(
        'Poppins', 10), width=80, height=5)

    label_death_text.grid(row=0, column=0, sticky=W)
    text_death.grid(row=1, column=0, columnspan=2, sticky=W)

    # Events
    frame_events = Frame(canvas_output, width=50, height=200, padx=5, pady=5)
    frame_events.grid(row=3, column=0, columnspan=3, padx=20)

    label_events_text = Label(frame_events, text='Events',
                              font=('Poppins', 13))
    text_events = Text(frame_events, wrap=WORD, font=(
        'Poppins', 10), width=80, height=5)

    label_events_text.grid(row=0, column=0, sticky=W)
    text_events.grid(row=1, column=0, columnspan=2, sticky=W)

    # Holidays
    frame_holidays = Frame(canvas_output, width=50, height=200, padx=5, pady=5)
    frame_holidays.grid(row=4, column=0, columnspan=3, padx=20)

    label_holidays_text = Label(frame_holidays, text='Holidays',
                                font=('Poppins', 13))
    text_holidays = Text(frame_holidays, wrap=WORD, font=(
        'Poppins', 10), width=80, height=5)

    label_holidays_text.grid(row=0, column=0, sticky=W)
    text_holidays.grid(row=1, column=0, columnspan=2, sticky=W)

    Label(canvas_output, text='', font=(
        'Poppins', 1)).grid(row=4, column=0)

    root.mainloop()
