ticketPrice = 10
ticketsRemaining = 100
serviceCharge = 2

def calcPrice(numberOfTickets):
    return numberOfTickets * ticketPrice + serviceCharge

while ticketsRemaining >=1:
    print('There are {} tickets remaining!'.format(ticketsRemaining))

    name = input('What is your name? ')

    print('Hey {}! Glad you are interested in our show!'.format(name))
    try:
        numberOfTickets = int(input('How many tickets would you like to purchase? '))
        if numberOfTickets > ticketsRemaining:
            raise ValueError('You can\'t purchase more than {} tickets'.format(ticketsRemaining))
    except ValueError as err:
        # Include the error text in the output
        print('Oh no! We ran into an error. {}. Try again.'.format(err))
    else:
        amountDue = calcPrice(numberOfTickets)

        print('You are going to purchase {} tickets for ${}.'.format(numberOfTickets, amountDue))

        choiceProceed = input('Would you like to to proceed to purchase? Please enter Y / N: ')

        if choiceProceed.lower() == 'y':
            # TODO: Gather credit card information and process it
            print('SOLD! Your purchase has been confirmed.')
            ticketsRemaining -= numberOfTickets
        else:
            print('Thank you for taking an interest in our show! Goodbye, {}.'.format(name))
else:
    print('We\'re sorry! Tickets are all sold out! Better luck next time, {}.'.format(name))
