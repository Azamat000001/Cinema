🎬 Cinema Seat Reservation System
👥 Group Members

Asatbekov Azamat
Urbaiev Nurislam
Dastanbek uulu Zhanybek


📖 Project Description
The Cinema Seat Reservation System is a Python desktop application that provides a visual cinema hall layout where users can select seats, apply discounts, and book tickets. A built-in cashier report tracks total revenue and ticket sales across the session.

❗ Problem Statement
Managing cinema seat bookings manually leads to double reservations and poor customer experience. There is a need for a simple digital tool that shows real-time seat availability and handles ticket pricing automatically.

✅ Solution Overview
The application displays a 5×8 seat grid. Each seat is color-coded by status. Users click seats to select them, choose a discount, and confirm the booking. Reserved seats are saved to a local file so the data persists between runs. A cashier panel shows session statistics.

🛠️ Technologies Used
TechnologyPurposePython 3.xCore programming languageTkinterGraphical User Interface (GUI)JSONSaving and loading seat reservation dataosChecking if the save file exists

▶️ Instructions to Run the Project

Make sure Python 3 is installed on your computer.
Clone or download this repository:

   git clone [https://github.com/your-repo-link-here.git](https://github.com/Azamat000001/Cinema)

Navigate to the project folder:

   cd cinema-reservation-system

Run the main file:

   python main.py

No third-party libraries needed — only Python's built-in modules are used (tkinter, json, os).


✨ Key Features

🪑 5×8 seat grid — interactive visual layout of the cinema hall
🟢 Free / 🟡 Selected / 🔴 Occupied — color-coded seat statuses
💰 Row-based pricing — VIP row ($15), Middle rows ($12), Budget rows ($8)
🏷️ Discount options — "Buy 3 Get 1 Free" or 15% off for groups of 6+
💾 Persistent data — seat reservations saved to hall.json and reloaded on startup
📊 Cashier report — shows total tickets sold, revenue, and occupied/free seat counts
🔄 Reset selection — deselect chosen seats before confirming a booking
