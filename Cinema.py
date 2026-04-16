ROWS = 5
SEATS = 8

hall = [[0 for _ in range(SEATS)] for _ in range(ROWS)]

total_revenue = 0
tickets_sold = 0

def get_price(row):
    return 15 if row == 0 else 12 if row <= 2 else 8

def show_hall():
    print("\nCinema Hall:")
    for i, row in enumerate(hall):
        print(f"R{i+1}", " ".join("O" if seat == 0 else "X" for seat in row))

def cashier():
    print("\n--- Cashier ---")
    print("Tickets sold:", tickets_sold)
    print("Revenue:", total_revenue)

def book_seats():
    global total_revenue, tickets_sold

    r = int(input("Row: ")) - 1
    s = int(input("Seat: ")) - 1

    if hall[r][s] == 0:
        price = get_price(r)
        hall[r][s] = 1
        total_revenue += price
        tickets_sold += 1
        print("Booked!")
    else:
        print("Occupied!")

while True:
    print("\n1. Show Hall")
    print("2. Book")
    print("3. Cashier")
    print("4. Exit")

    c = input("Choose: ")

    if c == "1":
        show_hall()
    elif c == "2":
        book_seats()
    elif c == "3":
        cashier()
    else:
        break
