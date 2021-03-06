import numpy as np
from copy import deepcopy as cp


class Deck:
    def __init__(self, n_decks):
        # because the color doesn't matter, we consider the a deck to have 13 cards
        self.n_decks = n_decks
        self.cards = []
        self.reset()

    def draw_card(self, card=None):
        if card is not None:
            new_deck = cp(self)
            if new_deck.cards[card] > 0:
                new_deck.cards[card] -= 1
                return new_deck
            else:
                return None
        else:
            if sum(self.cards) <= 0:
                self.reset()
            return np.random.choice([i for i in range(13)], p=self.get_prob())

    def add_card(self, card):
        new_deck = cp(self)
        new_deck.cards[card] += 1
        return new_deck

    def reset(self):
        self.cards = [self.n_decks * 4 for _ in range(13)]

    def get_prob(self):
        s = sum(self.cards)
        return [freq/s for freq in self.cards]
