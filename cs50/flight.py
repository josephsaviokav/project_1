class flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passenger=[]
    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True
    def open_seats(self):
        return self.capacity-len(self.passenger)
flight=flight(3)
people=['harry','ron','hemronie','slyhterine']
for person in people:
    sucess=flight.add_passenger(person)
    if sucess:
        print(f"Added {person} Sucessfully")
    else:
        print(f"No avaliable seats for {person}")
        