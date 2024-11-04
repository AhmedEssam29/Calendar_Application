# Calendar Application
A simple GUI-based Calendar Application created using Python and Tkinter, which allows users to view the calendar for any specified year.

## Project Overview
This Calendar Application provides a graphical interface to display the calendar of a user-selected year. By entering a year and clicking Show Calendar, users can view a complete calendar for that year within the application window.

## Table of Contents
1. [Features](#Features)
2. [Requirements](#Requirements)
3. [Installation and Usage](#Installation#and#Usage)
4. [Code Explanation](#Code#Explanation)
5. [App Interface](#AppInterface)

## Features
- Calendar Display: Shows the complete calendar of the specified year.
- User-Friendly Interface: Intuitive and easy-to-use interface for quick navigation.
- Cross-Platform Compatibility: Built with Tkinter, which runs on all major platforms with Python support.

## Requirements
- Python 3.x

- Tkinter: Tkinter is typically included with Python installations, but if not, install it via:

```bash
pip install tk
```
## Installation and Usage

1. Clone the repository or copy the provided code.

2. Ensure Python and Tkinter are installed on your system.

3. Run the application script using the command:

```bash
python calendar.py
```
4. The GUI will open, prompting the user to enter a year.

5. After entering a year, click Show Calendar to view the calendar for that year in a separate window.

6. To close the application, click Exit.

## Code Explanation
The code consists of two primary functions:

1. Main Interface Setup:

- A Tkinter window is initialized with labels, an input field for the year, and buttons for generating the calendar and exiting the application.
- Users enter a year and click Show Calendar to initiate the calendar display.

Calendar Display:

- The **show_calendar()** function opens a new window to display the calendar for the entered year.
- The Python **calendar** module is used to generate the calendar content, which is then displayed as text in a Tkinter label.
## Example Code Snippet
```bash
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
```


## App Interface
Below is an image of the Calendar Application interface:

![alt text](https://github.com/AhmedEssam29/Calendar_Application/blob/main/app2.png?raw=true)
