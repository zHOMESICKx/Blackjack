import os
import sys


class player:
    name = ""
    amount = 500.0
    cards = []
    bet = 0.0
    total = 0
    natural21 = False
    aceInHand = False
    dealer = False
    bust = False

    def endGame(self):
        """
        process to end game due to no amount remaining
        """
        if self.amount <= 0:
            print(
                f'Sorry {self.name}, you have played well but you have lost.')
            sys.exit()

    def placeBet(self):
        """
        process to allow player to place bet
        """
        while True:
            try:
                # placing bet
                bet = float(
                    input(f"You have {self.amount}. Please enter the amount you want to bet: "))

                # minimum bet of 1
                if bet < 1:
                    print("You have to place a minimum bet of 1 to play")
                    continue

                # amount is valid, storing amount in self.bet
                if bet <= self.amount:
                    self.bet = bet
                    self.amount -= bet
                    break
                else:
                    print("You have tried to bet more than you have.")
            except:
                # invalid input
                print("You have not entered a valid number.")

    def processCards(self, stick=False, pla=None):
        """
        process to work out total for cards in hand
        """
        os.system('cls')
        total = 0
        self.aceInHand = False

        # looping cards to build up total
        for card in self.cards:
            if card['number'] == 1:
                aceInHand = True

            if not self.dealer:
                print(f"{card['name']} of {card['set']}")

            total += card["value"]

        # checking if ace and working out if should be 11 or keep as 1
        if self.aceInHand and total <= 10:
            if not self.dealer:
                print(f"Total: {total} or {total + 10}")

            # keep total
            if total + 10 == 21 or stick:
                self.total = total = total + 10

            # dealer handling of ace
            if self.dealer:
                if total + 10 > pla.total:
                    self.amount = total + 10
                    return True
        else:
            if not self.dealer:
                print(f"Total: {total}")
            else:
                if total > pla.total:
                    return True

    def win(self, multiplier=2):
        """
        process to record and add winnings to player amount
        """
        print(
            f"You have won {self.bet * multiplier} with a score of {self.total}")
        self.amount += self.bet * 2

    def checkIfBust(self):
        """
        process to check if the user has lost, ie greater than 21
        """
        if self.total > 21:
            self.bust = True
            if not self.dealer:
                print(
                    f"Sorry {self.name} you have lost with a score of {self.total}")
                input('Press enter to start again:')
                os.system('cls')
            return True
        else:
            return False

    def ifStartingCardsWin(self):
        """
        process to check if user has a natural 21, auto win
        """
        # setting total to 0
        total = 0

        # for dealing with ace's
        for i in self.cards:
            if i['number'] == 1:
                total += 11
            else:
                total += i['value']

        # if total == 21 then process win return True
        if total == 21:
            self.win(multiplier=2.5)
            return True

        # printing cards
        self.processCards()


class dealer(player):
    dealer = True
