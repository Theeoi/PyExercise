"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division
from texttable import Texttable

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits: dict[str, int] = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self) -> None:
        """
        Builds a histogram of the ranks that appear in the hand.
        Stored in attribute ranks.
        """
        self.ranks: dict[str, int] = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_pair(self) -> bool:
        """
        Checks if hand contains a poker pair.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_two_pair(self) -> bool:
        """
        Checks if hand contains a poker two pair.
        """
        self.rank_hist()
        num_pairs = 0
        for val in self.ranks.values():
            if val >= 2:
                num_pairs += 1

        if num_pairs >= 2:
            return True

        return False

    def has_three(self) -> bool:
        """
        Checks if hand contains a poker three of a kind.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self) -> bool:
        """
        Checks if hand contains a poker straight.
        """
        rankslist = [card.rank for card in self.cards]
        ranks: tuple[int, ...] = tuple(set(sorted(rankslist)))
        if len(ranks) < 5:
            return False
        slen = 0
        for i, rank in enumerate(ranks[:-1]):
            if ranks[i+1] != rank + 1:
                slen = 0
            slen += 1
            # A very wonky "fix" for 10-J-Q-K-A straights
            if (i == len(ranks) - 2 and rank == 12 and ranks[0] == 1):
                slen += 1
            if slen >= 5:
                return True
        return False

    def has_house(self) -> bool:
        """
        Checks if hand contains a poker full house.
        """
        self.rank_hist()
        has_three = False
        has_pair = False
        for val in self.ranks.values():
            if val >= 3:
                has_three = True
                continue
            if val >= 2:
                has_pair = True

        if has_three and has_pair:
            return True
        return False

    def has_four(self) -> bool:
        """
        Checks if hand contains a poker four of a kind.
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def has_straight_flush(self) -> bool:
        """
        Checks if hand contains poker straight flush.
        """
        for suit in range(4):
            suit_rankslist = []
            for card in self.cards:
                if card.suit == suit:
                    suit_rankslist.append(card.rank)
            suit_ranks: tuple[int, ...] = tuple(set(sorted(suit_rankslist)))
            if len(suit_ranks) >= 5:
                # This code does not work for 10-J-Q-K-A straights
                # since rank[K] = 13 and rank[A] = 1
                slen = 0
                for i, rank in enumerate(suit_ranks[:-1]):
                    if suit_ranks[i+1] != rank + 1:
                        slen = 0
                    slen += 1
                    # A very wonky "fix" for 10-J-Q-K-A straights
                    if (i == len(suit_ranks) - 2 and rank == 12 and suit_ranks[0] == 1):
                        slen += 1
                    if slen >= 5:
                        return True

        return False

    def classification(self) -> None:
        """
        Sets the label of the hand to the highest value classification.
        """
        labels: tuple[str, ...] = ('None', 'Pair', 'Two pairs',
                                   'Three of a kind', 'Straight', 'Flush',
                                   'Full house', 'Four of a kind',
                                   'Straight flush')
        classification: dict[str, int] = {'has_pair': 1, 'has_two_pair': 2,
                                          'has_three': 3, 'has_straight': 4,
                                          'has_flush': 5, 'has_house': 6,
                                          'has_four': 7, 'has_straight_flush': 8}
        checkers: list[str] = [f for f in dir(self) if f.startswith('has')]
        label_index: list[int] = [0]

        for checker in checkers:
            func = getattr(self, checker)
            if func():
                label_index.append(classification[checker])

        self.label = labels[max(label_index)]


def count_classifications(num: int, hand_size: int = 7, p_out: bool = True) -> dict[str, int]:
    """
    Deals {num} hands and returns a dict mapping hand labels to their
    frequency.
    """
    label_hist: dict[str, int] = {}
    for _ in range(num):
        deck = Deck()
        deck.shuffle()

        hand = PokerHand()
        deck.move_cards(hand, hand_size)

        hand.classification()
        label_hist[hand.label] = label_hist.get(hand.label, 0) + 1

    if p_out:
        print_pokerprob(label_hist)

    return label_hist


def print_pokerprob(label_hist: dict[str, int]) -> None:
    """
    Prints table of simulated poker hand probabilities.
    """
    num_sim: int = sum(label_hist.values())
    table = Texttable()
    table.header(["Type", "Frequency", "Probability"])
    table.set_cols_dtype(['t', 'i', 't'])
    for key, value in label_hist.items():
        table.add_row([key, value, f"{(value/num_sim)*100:.2f}"])

    table.set_deco(Texttable.HEADER | Texttable.BORDER)
    print(table.draw())


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for _ in range(0):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print('')

        hand.classification()
        print(hand.label)

    NUM_HANDS: int = 100000
    label_hist: dict[str, int] = count_classifications(NUM_HANDS)
