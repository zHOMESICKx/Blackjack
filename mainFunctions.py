import random


class mainFunctions:
    deck = []

    def __init__(self):
        """
        init function of class
        """
        self.populateDeck()

    def populateDeck(self):
        """
        function to populate the deck to save time writing every possible card
        """
        # loopping all sets and cards
        for cardSet in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for cardNumber in range(1, 14):
                if cardNumber > 10:
                    value = 10
                    if cardNumber == 11:
                        cardName = "Jack"
                    if cardNumber == 12:
                        cardName = "Queen"
                    if cardNumber == 13:
                        cardName = "King"
                else:
                    if cardNumber == 1:
                        cardName = "Ace"
                    else:
                        cardName = str(cardNumber)
                    value = cardNumber

                # appending card to deck
                self.deck.append(
                    {
                        "set": cardSet,
                        "number": cardNumber,
                        "name": cardName,
                        "value": value
                    }
                )

    def populateStartCards(self, pla):
        """
        function to populate starting cards of the game and to remove them from the deck
        """
        # reset figures
        pla.startingCards = True
        pla.cards = []
        pla.aceInHand = False
        pla.total = 0

        # 2 loops for the starting cards
        for i in range(0, 2):
            pla = self.addCard(pla)
        pla.startingCards = True
        return pla

    def addCard(self, pla):
        """
        function to add card to players hand
        """
        if not self.deck:
            self.populateDeck()
        card = random.choice(self.deck)
        pla.cards.append(card)
        pla.total = pla.total + card['value']
        self.deck.remove(card)
        return pla
