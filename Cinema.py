ROWS = 5
SEATS = 8

hall = [[0 for _ in range(SEATS)] for _ in range(ROWS)]

def get_price(row):
    if row == 0:
        return 15
    elif row <= 2:
        return 12
    return 8

def apply_discount(count, total):
    if count >= 4:
        return total - 8
    return total

def show_hall():
    print("\nCinema Hall:")
    for i, row in enumerate(hall):
        print(f"R{i+1}", " ".join("O" if seat == 0 else "X" for seat in row))

def book_seats():
    count = int(input("How many seats: "))
    total = 0

    for _ in range(count):
        r = int(input("Row: ")) - 1
        s = int(input("Seat: ")) - 1

        if 0 <= r < ROWS and 0 <= s < SEATS:
            if hall[r][s] == 0:
                hall[r][s] = 1
                total += get_price(r)
            else:
                print("Occupied!")

    total = apply_discount(count, total)
    print("Total:", total)

while True:
    print("\n1. Show Hall")
    print("2. Book Seats")
    print("3. Exit")

    c = input("Choose: ")

    if c == "1":
        show_hall()
    elif c == "2":
        book_seats()
    elif c == "3":
        break
