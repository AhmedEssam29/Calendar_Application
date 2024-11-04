# Importing tkinter module
from tkinter import *
# Importing calendar module
import calendar

# Function to show the calendar of the given year
def show_calendar():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar for the Year")
    gui.geometry("550x600")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    cal_year = Label(gui, text=gui_content, font="Consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20)
    gui.mainloop()

# Driver code
if __name__ == '__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendar")
    new.geometry("250x140")

    # Creating labels and input field
    cal_label = Label(new, text="Calendar", bg='grey', font=("times", 28, "bold"))
    year_label = Label(new, text="Enter Year", bg='dark grey')
    year_field = Entry(new)

    # Show calendar button
    show_button = Button(new, text='Show Calendar', fg='Black', bg='Blue', command=show_calendar)

    # Exit button to close the application
    exit_button = Button(new, text="Exit", fg='Black', bg='Red', command=new.destroy)

    # Placing widgets on the grid
    cal_label.grid(row=1, column=1)
    year_label.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    show_button.grid(row=4, column=1)
    exit_button.grid(row=5, column=1)

    new.mainloop()
