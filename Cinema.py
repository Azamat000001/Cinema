ROWS = 5
SEATS = 8

hall = [[0 for _ in range(SEATS)] for _ in range(ROWS)]

def get_price(row):
    if row == 0:
        return 15
    elif row <= 2:
        return 12
    return 8

def show_hall():
    print("\nCinema Hall:")
    for i, row in enumerate(hall):
        print(f"R{i+1}", " ".join("O" if seat == 0 else "X" for seat in row))

def book_seat():
    r = int(input("Row: ")) - 1
    s = int(input("Seat: ")) - 1

    if 0 <= r < ROWS and 0 <= s < SEATS:
        if hall[r][s] == 0:
            hall[r][s] = 1
            print("Booked! Price:", get_price(r))
        else:
            print("Seat occupied!")
    else:
        print("Invalid seat!")

while True:
    print("\n1. Show Hall")
    print("2. Book Seat")
    print("3. Exit")

    c = input("Choose: ")

    if c == "1":
        show_hall()
    elif c == "2":
        book_seat()
    elif c == "3":
        break
