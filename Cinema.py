import tkinter as tk
from tkinter import messagebox
import json
import os

ROWS = 5
SEATS = 8
FILE = "hall.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return [[0 for _ in range(SEATS)] for _ in range(ROWS)]

def save_data():
    with open(FILE, "w") as f:
        json.dump(hall, f)

hall = load_data()
selected = []

total_revenue = 0
total_tickets_sold = 0

def get_price(row):
    if row == 0:
        return 15
    elif row <= 2:
        return 12
    else:
        return 8

def update_info():
    total = sum(get_price(r) for r, s in selected)
    info_label.config(text=f"Selected: {len(selected)} | Total: ${total:.2f}")

def toggle_seat(r, s):
    if hall[r][s] == 1:
        messagebox.showwarning("Error", "Seat already occupied!")
        return

    btn = buttons[r][s]

    if (r, s) in selected:
        selected.remove((r, s))
        btn.config(bg="lightgreen")
    else:
        selected.append((r, s))
        btn.config(bg="yellow")

    update_info()

def book_seats():
    global total_revenue, total_tickets_sold

    if not selected:
        messagebox.showinfo("Info", "No seats selected!")
        return

    total = sum(get_price(r) for r, s in selected)
    final = total

    discount = discount_var.get()

    if discount == "3=4" and len(selected) >= 4:
        free = len(selected) // 4
        cheapest = min(get_price(r) for r, s in selected)
        final -= cheapest * free

    elif discount == "15%" and len(selected) > 5:
        final *= 0.85

    for r, s in selected:
        hall[r][s] = 1
        buttons[r][s].config(bg="red")

    save_data()

    total_revenue += final
    total_tickets_sold += len(selected)

    selected.clear()
    update_info()

    messagebox.showinfo("Success", f"Booked!\nTotal: ${final:.2f}")

def reset_selection():
    for r, s in selected:
        if hall[r][s] == 0:
            buttons[r][s].config(bg="lightgreen")
    selected.clear()
    update_info()

def show_stats():
    occupied = sum(seat for row in hall for seat in row)

    messagebox.showinfo(
        "Cashier Report",
        f"Tickets sold: {total_tickets_sold}\n"
        f"Revenue: ${total_revenue:.2f}\n"
        f"Occupied: {occupied}\n"
        f"Free: {ROWS * SEATS - occupied}"
    )

root = tk.Tk()
root.title("🎬 Cinema Booking System")
root.geometry("600x500")

title = tk.Label(root, text="Cinema Hall", font=("Arial", 18, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = []

for i in range(ROWS):
    row_buttons = []
    for j in range(SEATS):
        color = "lightgreen" if hall[i][j] == 0 else "red"

        btn = tk.Button(
            frame,
            text=f"{i+1}-{j+1}",
            width=5,
            height=2,
            bg=color,
            command=lambda r=i, s=j: toggle_seat(r, s)
        )
        btn.grid(row=i, column=j, padx=3, pady=3)
        row_buttons.append(btn)
    buttons.append(row_buttons)

legend = tk.Label(root, text="🟢 Free   🟡 Selected   🔴 Occupied")
legend.pack()

info_label = tk.Label(root, text="Selected: 0 | Total: $0.00")
info_label.pack()

discount_var = tk.StringVar(value="None")

frame2 = tk.Frame(root)
frame2.pack()

tk.Label(frame2, text="Discount: ").pack(side="left")
tk.Radiobutton(frame2, text="None", variable=discount_var, value="None").pack(side="left")
tk.Radiobutton(frame2, text="3=4", variable=discount_var, value="3=4").pack(side="left")
tk.Radiobutton(frame2, text="15%", variable=discount_var, value="15%").pack(side="left")

btns = tk.Frame(root)
btns.pack()

tk.Button(btns, text="Book", command=book_seats).pack(side="left")
tk.Button(btns, text="Reset", command=reset_selection).pack(side="left")
tk.Button(btns, text="Stats", command=show_stats).pack(side="left")
tk.Button(btns, text="Exit", command=root.quit).pack(side="left")

root.mainloop()
