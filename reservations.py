import tkinter as tk
from tkinter import ttk, messagebox
from database import get_reservations, delete_reservation

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        heading = tk.Label(self, text="All Reservations", font=("Arial", 20, "bold"))
        heading.pack(pady=20)

        # Table
        columns = ("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110, anchor="center")

        self.tree.pack(fill="both", expand=True)

        # Buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        refresh_btn = tk.Button(btn_frame, text="Refresh", command=self.load_data)
        refresh_btn.grid(row=0, column=0, padx=5)

        edit_btn = tk.Button(btn_frame, text="Edit", command=self.edit_selected)
        edit_btn.grid(row=0, column=1, padx=5)

        delete_btn = tk.Button(btn_frame, text="Delete", command=self.delete_selected)
        delete_btn.grid(row=0, column=2, padx=5)

        back_btn = tk.Button(btn_frame, text="Back to Home",
                             command=lambda: controller.show_frame("HomePage"))
        back_btn.grid(row=0, column=3, padx=5)

        # Load initial data
        self.load_data()

    def load_data(self):
        """Fetch reservations from DB and display"""
        # Clear old data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Get fresh data
        reservations = get_reservations()
        for row in reservations:
            self.tree.insert("", "end", values=row)

    def get_selected(self):
        """Return selected row data"""
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation first.")
            return None
        return self.tree.item(selected, "values")

    def edit_selected(self):
        """Open Edit page for selected reservation"""
        row = self.get_selected()
        if row:
            self.controller.show_edit_page(row)  # Pass row to main.py handler

    def delete_selected(self):
        """Delete selected reservation"""
        row = self.get_selected()
        if row:
            res_id = row[0]
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reservation?")
            if confirm:
                delete_reservation(res_id)
                self.load_data()
                messagebox.showinfo("Deleted", "Reservation deleted successfully.")
