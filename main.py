import tkinter as tk
from tkinter import *
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage
import os

class FlightApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Flight Reservation System")
        self.geometry("800x600")
        # Set icon
        icon_path = r"C:\Courses\Sprints x Microsoft Summer Camp - Programming using Python\Python\flight_reservation_app\flight.ico"
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)
        else:
            print("⚠️ Icon file not found:", icon_path)

        # Dictionary to hold pages
        self.frames = {}

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # make the single grid cell inside `container` expand when window is resized
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # optional: ensure the root also lets the container expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Initialize pages
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

    def show_edit_page(self, reservation):
        """Open edit page with selected reservation data"""
        frame = self.frames["EditReservationPage"]
        frame.load_reservation(reservation)
        frame.tkraise()

if __name__ == "__main__":
    app = FlightApp()
    app.mainloop()
