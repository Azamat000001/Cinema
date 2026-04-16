ROWS = 5
SEATS = 8

hall = [[0 for _ in range(SEATS)] for _ in range(ROWS)]

def show_hall():
    print("\nCinema Hall:")
    for row in hall:
        print(" ".join("O" if seat == 0 else "X" for seat in row))

while True:
    print("\n1. Show Hall")
    print("2. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_hall()
    elif choice == "2":
        break
