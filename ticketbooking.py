class Booking():
    def __init__(self,name,train_no,amount,seats):
        self.name=name
        self.train_no=train_no
        self.amount=amount
        self.seats=seats
    def information(self):
        print(25*"-")
        print("your train name is:",self.name)
        print("your train number is:",self.train_no)
        print("Available seats in the train is:",self.seats)
        print(25*"-")

    def ticketBooking(self):
        if(self.seats>=0):
            print("your ticket is succussfully confirmed...")
            print("your seat number is:",self.seats)
            self.seats=self.seats-1
        else:
            print("there are no seats available in the train...")
        
    def amountDetails(self):
        print("your ticket amount is:",self.amount)


    
obj=Booking("metro",12345,250,4)
obj.information()
obj.amountDetails()
obj.ticketBooking()
obj.information()

