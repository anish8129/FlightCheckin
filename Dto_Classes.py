
class ReservationUpdateRequest:
    def __init__(self, id, checkedin,number_of_bags):
        self.id =id
        self.checked_in = checkedin
        self.number_of_bags = number_of_bags

class Passenger :
    def __init__(self, id, f_name, l_name,email,phone):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.phone = phone
        

class Flight :
    def __init__(self, id, flight_number, operating_airlines, 
    departure_city, arrival_city, departure_date, estimated_departure_time):
        self.id = id
        self.flight_number = flight_number
        self.operating_airlines = operating_airlines
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_date = departure_date
        self.estimated_departure_time = estimated_departure_time


class Reservation :
    def __init__(self, id,checked_in,number_of_bags,passenger,flight):
        self.id = id
        self.checked_in = checked_in
        self.number_of_bags = number_of_bags
        self.passenger = passenger
        self.flight = flight
