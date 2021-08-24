#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle
from collections import deque


# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def _compare(card1, card2):
    if RANKS.index(card1[1:]) > RANKS.index(card2[1:]):
        return 1
    if RANKS.index(card1[1:]) == RANKS.index(card2[1:]):
        return 0
    return -1

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    deck = []
    def __init__(self):
        for s in SUITE:
            for r in RANKS:
                self.deck.append(s+r)

    def shuffle_and_split(self):
        shuffle(self.deck)
        return self.deck[:26], self.deck[26:]



class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = deque(cards)

    def add_cards(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        if self.has_cards:
            return self.cards.popleft()
        return -1

    def has_cards(self):
        if self.cards:
            return True
        return False


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    def lost(self):
        if self.hand.has_cards():
            return False
        else:
            return True
    def draw_card(self):
        if self.hand.has_cards():
            return 1, self.hand.remove_card()
        else:
            return 0, None
    def draw_three_cards(self):
        card_pool = []
        for _ in range(3):
            new_sig, card = self.draw_card()
            if new_sig == 0:
                return 0, card_pool
            card_pool.append(card)
        return 1, card_pool

    def take_all_cards(self, table):
        self.hand.add_cards(table)
        while table:
            table.pop()
    def _display(self):
        print(f"{self.name} card count: {len(self.hand.cards)}")



######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
d = Deck()
half1, half2 = d.shuffle_and_split()
name = input('What is your name?\n')
computer = Player('Computer', Hand(half1))
player = Player(name, Hand(half2))


table = []
round_cnt = 1

game_over = 0


while not (computer.lost() or player.lost()):
    player._display()
    computer._display()
    sig_comp, computer_card = computer.draw_card()
    sig_player, player_card = player.draw_card()
    table.append(computer_card)
    table.append(player_card)
    print(f"{round_cnt} round")
    
    while _compare(computer_card, player_card) == 0:
        print(f'{player.name}: {player_card}')
        print(f'{computer.name}: {computer_card}')
        print('There is a tie... Drawing four more cards')
        sig_comp, computer_cards = computer.draw_three_cards()
        sig_player, player_cards = computer.draw_three_cards()
        if not (sig_comp and sig_player):
            game_over = 1
            break
        table.extend(computer_cards)
        table.extend(player_cards)

        sig_comp, computer_card = computer.draw_card()
        sig_player, player_card = player.draw_card()
        table.append(computer_card)
        table.append(player_card)
        if not (sig_comp and sig_player):
            game_over = 1
            break



    if game_over:
        print('We have a winner!')
        break
    print('Table - ')
    print(table)

    print(f'{player.name}: {player_card}')

    print(f'{computer.name}: {computer_card}')
    if _compare(computer_card, player_card) == 1:
        print('Computer wins this around and take all cards')
        computer.take_all_cards(table)
    else:
        player.take_all_cards(table)
        print(name + ' wins this around and take all cards')
    round_cnt += 1

if computer.lost():
    print(name + ' wins')
else:
    print('The computer wins.')




# Use the 3 classes along with some logic to play a game of war!






