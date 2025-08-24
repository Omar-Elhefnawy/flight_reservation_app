import tkinter as tk
from tkinter import *


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f8f9fa")  # light background
        self.controller = controller

        header = Frame(self, bg="#0284c7")
        header.pack(fill=X)

        title_label = Label(header,
                    text="Flight Reservation App",
                    fg="#FFFFFF",
                    bg="#0284c7",
                    padx=12,
                    pady=10,
                    font=("Courier", 24))
        title_label.pack(side=LEFT)

        # Subheading
        subheading = tk.Label(
            self,
            text="Book your flights and manage your reservations\nwith our simple and intuitive system.",
            font=("Arial", 14),
            fg="#495057",
            bg="#f8f9fa"
        )
        subheading.pack(pady=(0, 70))

        # Container for "cards"
        cards_frame = tk.Frame(self, bg="#f8f9fa")
        cards_frame.pack(pady=20)

        # --- Book Flight Card ---
        book_card = tk.Frame(cards_frame, bg="white", bd=1, relief="solid", padx=30, pady=30)
        book_card.grid(row=0, column=0, padx=30)

        book_icon = tk.Label(book_card, text=" ✈", font=("Arial", 40), fg="#0d6efd", bg="white")
        book_icon.pack(pady=10)

        book_title = tk.Label(book_card, text="Book a Flight", font=("Arial", 18, "bold"), bg="white")
        book_title.pack(pady=5)

        book_desc = tk.Label(book_card,
                             text="Reserve your next flight by providing your details\nand flight information.",
                             font=("Arial", 12),
                             fg="#6c757d",
                             bg="white",
                             justify="center")
        book_desc.pack(pady=10)

        book_btn = tk.Button(
            book_card,
            text="Book Flight",
            font=("Arial", 12, "bold"),
            bg="#0d6efd",
            fg="white",
            relief="flat",
            padx=15,
            pady=5,
            command=lambda: controller.show_frame("BookingPage")
        )
        book_btn.pack(pady=10)

        # --- View Reservations Card ---
        view_card = tk.Frame(cards_frame, bg="white", bd=1, relief="solid", padx=30, pady=30)
        view_card.grid(row=0, column=1, padx=30)

        view_icon = tk.Label(view_card, text="📋", font=("Arial", 40), fg="#0d6efd", bg="white")
        view_icon.pack(pady=10)

        view_title = tk.Label(view_card, text="View Reservations", font=("Arial", 18, "bold"), bg="white")
        view_title.pack(pady=5)

        view_desc = tk.Label(view_card,
                             text="Manage your existing reservations, view details,\nedit or cancel if needed.",
                             font=("Arial", 12),
                             fg="#6c757d",
                             bg="white",
                             justify="center")
        view_desc.pack(pady=10)

        view_btn = tk.Button(
            view_card,
            text="View Reservations",
            font=("Arial", 12, "bold"),
            bg="#0d6efd",
            fg="white",
            relief="flat",
            padx=15,
            pady=5,
            command=lambda: controller.show_frame("ReservationsPage")
        )
        view_btn.pack(pady=10)
