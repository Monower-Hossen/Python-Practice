'''6. Can you change the self-parameter inside a class to something else (say
“monower”). Try changing self to “slf” or “monower” and see the effects'''

from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(monower, fro, to):
        print(f"Ticket is booked in train no: {monower.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time") 

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")  


t = Train(12399)
t.book("Dhaka", "mymensingh")
t.getStatus()
t.getFare("Rampur", "Delhi")


