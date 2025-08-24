import tkinter as tk
from tkinter import *
import database as db
from database import add_reservation
db.connect()
db.create_table()

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        heading = tk.Label(self, text="Book a Flight", font=("Arial", 20, "bold"))
        heading.pack(pady=20)

        cards_frame = tk.Frame(self, bg="#f8f9fa")
        cards_frame.pack(pady=20)

        book_card = tk.Frame(cards_frame, bg="white", bd=1, relief="solid", padx=100, pady=100)
        book_card.grid(row=0, column=0, padx=30)
        
                # Input fields (placed inside book_card using grid)
        self.name_var = tk.StringVar()
        self.flight_var = tk.StringVar()
        self.departure_var = tk.StringVar()
        self.destination_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.seat_var = tk.StringVar()

        labels = [
            ("Passenger Name", self.name_var),
            ("Flight Number", self.flight_var),
            ("Departure", self.departure_var),
            ("Destination", self.destination_var),
            ("Date", self.date_var),
            ("Seat Number", self.seat_var),
        ]

        for i, (text, var) in enumerate(labels):
            tk.Label(book_card, text=text, bg="white").grid(row=i, column=0, sticky="w", pady=6)
            tk.Entry(book_card, textvariable=var, width=30).grid(row=i, column=1, pady=6, padx=(10,0))
        

        submit_btn = tk.Button(self, bg="#0d6efd", fg="white", text="Submit", font=("Arial", 16),
                               command=self.save_booking)
        submit_btn.pack(pady=20)

        back_btn = tk.Button(self, bg="#0d6efd", fg="white", text="Back to Home", font=("Arial", 16),
                             command=lambda: controller.show_frame("HomePage"))
        back_btn.pack(pady=10)



    def save_booking(self):
        name = self.name_var.get()
        flight = self.flight_var.get()
        departure = self.departure_var.get()
        destination = self.destination_var.get()
        date = self.date_var.get()
        seat = self.seat_var.get()
         # Simple validation
        if name and flight and departure and destination and date and seat:
            add_reservation(name, flight, departure, destination, date, seat)  # ✅ insert into DB
            msg = Label(self, text="Reservation saved successfully!", fg="green", font=("Arial", 12))
            msg.pack()

            # Clear form after saving
            self.name_var.set("")
            self.flight_var.set("")
            self.departure_var.set("")
            self.destination_var.set("")
            self.date_var.set("")
            self.seat_var.set("")
            
        else:
            msg2= Label(self, text="All fields are required!", fg="red", font=("Arial", 12))
            msg2.pack()
            
