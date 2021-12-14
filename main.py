import os
import time

from mainFunctions import mainFunctions
from player import player, dealer


class game(mainFunctions):
    def main(self):
        """
        main function for game
        """
        # defining dealer and player
        pla = player()
        dea = dealer()

        # enter players name
        while True:
            try:
                pla.name = str(input("Please enter your name: "))
                break
            except:
                print("Please enter a valid option")

        # print name and rules
        os.system('cls')
        print(f"Hello {pla.name}, time to play some Blackjack!")

        while True:
            # place bet
            pla.placeBet()

            # populate starting cards and print what cards you have
            pla = self.populateStartCards(pla)
            dea = self.populateStartCards(dea)

            # if natural 21 then win
            if pla.ifStartingCardsWin():
                continue

            # entering what option you want
            while True:
                # forced stick if pla.toal is 21
                if pla.total == 21:
                    pla.processCards(stick=True)
                    break

                while True:
                    try:
                        # getting choice from user
                        error = 'You have not entered a valid option'
                        choice = int(input("0 = Stick 1 = Hit: "))
                        if choice in [0, 1]:
                            break
                        else:
                            print(error)
                            time.sleep(1)
                    except:
                        print(error)
                        time.sleep(1)

                # process choice
                if choice == 0:
                    # stick
                    pla.processCards(stick=True)
                    break
                else:
                    # hit me
                    pla = self.addCard(pla)
                    pla.processCards()
                    if pla.checkIfBust():
                        break

            # dealer get more cards or stick
            if not pla.bust and not pla.natural21:
                while True:
                    # checking if dealer has bust
                    if dea.checkIfBust():
                        print(f"Dealer has bust with a score of {dea.total}")
                        pla.win()
                        break
                    else: 
                        # checking if dealer won
                        if dea.processCards(pla=pla):
                            print(
                                f'Dealer has won with a score of {dea.total}')
                            input('Press Enter to play again')
                            break

                    # dealer get card
                    dea = self.addCard(dea)


run = game()
run.main()
