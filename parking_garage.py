class parkingGarage():
    current_ticket = {'paid': True}

    def __init__(self, tickets, spaces, current_ticket):
        self.tickets = tickets
        self.spaces = spaces
        self.current_ticket = current_ticket
        if self.tickets < 5:
            self.current_ticket['paid'] = False

    def takeTicket(self):
        take = input('take a ticket? y/n: ')
        if take == 'y':
            if self.tickets == 0:
                print('sorry, no tix left')
            else:
                self.tickets = self.tickets - 1 
                self.spaces = self.spaces - 1
                self.current_ticket['paid'] = False

    def payForParking(self):
        if self.spaces >= 5:
            print('You dont have a ticket. this is awkward.')
        else:
            amt_paid = input('How much are you paying? ')
            while True:
                    if amt_paid == '':
                        print('money, please: ')
                        amt_paid = input('how much?!')
                    if amt_paid != '':
                        print("tix paid. You have 15 min to leave or you will be trapped forever!")
                        self.current_ticket['paid'] = True
                        self.tickets = self.tickets + 1 
                        self.spaces = self.spaces + 1
                        break

    def leaveGarage(self):
        if self.current_ticket == {}:
            take = input('ticket not taken. take ticket? y/n: ')
            if take == 'y':
                self.tickets = self.tickets - 1 
                self.spaces = self.spaces - 1
                self.current_ticket['paid'] = False
            else:
                while True:
                    take2 = input('You should really press "y"')
                    if take2 != 'y':
                        take2 = input('seriously, press "y"')
                        if take2 == 'y':
                            self.current_ticket['paid'] = False
                            self.tickets = self.tickets - 1 
                            self.spaces = self.spaces - 1
                            print(f'**there are {self.tickets} tickets and {self.spaces} spaces left')
                            break
                    else:
                        self.current_ticket['paid'] = False
                        self.tickets = self.tickets - 1 
                        self.spaces = self.spaces - 1
                        print(f'**there are {self.tickets} tickets and {self.spaces} spaces left')
                        break
                    
        if self.current_ticket['paid'] == True:
            while self.tickets < 5:
                    print(f'{5 - self.tickets} tix unpaid. Pay now!')
                    amt_paid = input('How much are you paying? ')
                    if amt_paid == '':
                        print('money, please: ')
                        amt_paid = input('how much?!')
                    if amt_paid != '':
                        print("tix paid. You have 15 min to leave or you will be trapped forever!")
                        self.current_ticket['paid'] = True
                        self.tickets = self.tickets + 1 
                        self.spaces = self.spaces + 1
            else:
                print('thank you, have a nice day!')
        else:
            print('You have tix, pay me now!')
            amt_paid = input('How much are you paying? ')
            while True:
                if amt_paid == '':
                    print('money, please: ')
                    amt_paid = input('how much?!')
                else:
                    print("tix paid. You have 15 min to leave or you will be trapped forever!")
                    self.current_ticket['paid'] = True
                    self.tickets = self.tickets + 1 
                    self.spaces = self.spaces + 1
                    break
    
    def showTix(self):
        print(f'**there are {self.tickets} tickets and {self.spaces} spaces left')
            
my_garage = parkingGarage(5, 5, {})

my_garage.showTix()
my_garage.takeTicket()
my_garage.showTix()
my_garage.takeTicket()
my_garage.showTix()
my_garage.takeTicket()
my_garage.showTix()
my_garage.takeTicket()
my_garage.showTix()
my_garage.takeTicket()
my_garage.showTix()
my_garage.takeTicket()
my_garage.showTix()

my_garage.leaveGarage()
my_garage.showTix()

my_garage.payForParking()
my_garage.showTix()

my_garage.leaveGarage()
my_garage.showTix()