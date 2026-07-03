#EC1: Movie Ticket Software

print("Available movies today:")
print("A)12 Strong:   1)2:30  2)4:40 3)7:50 4)10:50")
print("B)Coco:        1)12:40 2)3:45")
print("C)The Post:    1)12:45 2)3:35 3)7:05 4)9:55")

movie = input("Movie choice: ")

if movie == 'A':
    time = int(input("Showtime: "))

    if time <= 4:
        numAdult = int(input("Adult tickets: "))
        numKid = int(input("Kid tickets: "))

        if (numAdult + numKid) <= 30:
            price = (numAdult * 12.45) + (numKid * 9.68)
            print(f"Total cost: ${price:.2f}")

if movie == 'B':
    time = int(input("Showtime: "))

    if time == 2:
        numAdult = int(input("Adult tickets: "))
        numKid = int(input("Kid tickets: "))

        if (numAdult + numKid) <= 30:
            price = (numAdult * 12.45) + (numKid * 9.68)
            print(f"Total cost: ${price:.2f}")

    if time == 1:
        numAdult = int(input("Adult tickets: "))
        numKid = int(input("Kid tickets: "))

        if (numAdult + numKid) <= 30:
            price = (numAdult * 11.17) + (numKid * 8.00)
            print(f"Total cost: ${price:.2f}")

if movie == 'C':
    time = int(input("Showtime: "))

    if time == 2 or 3 or 4:
        numAdult = int(input("Adult tickets: "))
        numKid = int(input("Kid tickets: "))
        if (numAdult + numKid) <= 30:
            price = (numAdult * 12.45) + (numKid * 9.68)
            print(f"Total cost: ${price:.2f}")

    if time == 1:
        numAdult = int(input("Adult tickets: "))
        numKid = int(input("Kid tickets: "))
        if (numAdult + numKid) <= 30:
            price = (numAdult * 11.17) + (numKid * 8.00)
            print(f"Total cost: ${price:.2f}")

else:
    print("Invalid option; please restart app...")