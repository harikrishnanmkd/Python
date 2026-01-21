class Movie:
    def __init__(self, title, available_seats):
        self.title = title
        self.available_seats = available_seats

    def book_ticket(self, seats):
        if seats <= self.available_seats:
            self.available_seats -= seats
            print(f"{seats}tickets booked successfully.")
        else:
            print("Not enough seats...")
title=input("Movie Name: ")
available_seats=int(input("Enter available seats:"))
movie=Movie(title,available_seats)


while True:
    seat=int(input("Enter seats to book:"))
    movie.book_ticket(seat)
    