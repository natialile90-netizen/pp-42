class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

        MovieTicket.total_tickets_sold += 1


ticket1 = MovieTicket("Titanic", "A1", 15)
ticket2 = MovieTicket("Avatar", "B5", 20)
ticket3 = MovieTicket("Inception", "C3", 18)

for ticket in [ticket1, ticket2, ticket3]:
    print("Cinema:", ticket.cinema_name)
    print("Movie:", ticket.movie_title)
    print("Seat:", ticket.seat_number)
    print("Price:", ticket.price)
    print("----------------")

print("Total tickets sold:", MovieTicket.total_tickets_sold)
