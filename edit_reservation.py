import tkinter as tk
from database import update_reservation, delete_reservation

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.reservation = None  # will hold selected row

        self.heading = tk.Label(self, text="Edit Reservation", font=("Arial", 20, "bold"))
        self.heading.pack(pady=20)

        # Variables
        self.name_var = tk.StringVar()
        self.flight_var = tk.StringVar()
        self.departure_var = tk.StringVar()
        self.destination_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.seat_var = tk.StringVar()

        tk.Label(self, text="Passenger Name").pack()
        tk.Entry(self, textvariable=self.name_var).pack()

        tk.Label(self, text="Flight Number").pack()
        tk.Entry(self, textvariable=self.flight_var).pack()

        tk.Label(self, text="Departure").pack()
        tk.Entry(self, textvariable=self.departure_var).pack()

        tk.Label(self, text="Destination").pack()
        tk.Entry(self, textvariable=self.destination_var).pack()

        tk.Label(self, text="Date").pack()
        tk.Entry(self, textvariable=self.date_var).pack()

        tk.Label(self, text="Seat Number").pack()
        tk.Entry(self, textvariable=self.seat_var).pack()

        update_btn = tk.Button(self, text="Update", font=("Arial", 14), command=self.update_res)
        update_btn.pack(pady=10)

        back_btn = tk.Button(self, text="Back to Reservations",
                             command=lambda: controller.show_frame("ReservationsPage"))
        back_btn.pack(pady=10)

    def load_reservation(self, reservation):
        """Load selected reservation into form"""
        self.reservation = reservation
        self.id = reservation[0]
        self.name_var.set(reservation[1])
        self.flight_var.set(reservation[2])
        self.departure_var.set(reservation[3])
        self.destination_var.set(reservation[4])
        self.date_var.set(reservation[5])
        self.seat_var.set(reservation[6])

    def update_res(self):
        update_reservation(
            self.id,
            self.name_var.get(),
            self.flight_var.get(),
            self.departure_var.get(),
            self.destination_var.get(),
            self.date_var.get(),
            self.seat_var.get()
        )
        self.controller.show_frame("ReservationsPage")
