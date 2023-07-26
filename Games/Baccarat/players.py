class InvalidBet(Exception):
    pass

class Player:
    """A player of baccarat game. Create several instances to have multiplayer.

    Args:
        pUserName: str, the username of the player.
        pCredit: int, the initial credit balance of the player.
        pMoneyMade: int, the total money made by the player.
        pMoneyLost: int, the total money lost by the player.
        currGame: str, the current game the player is playing.
        pWin: int, the total number of wins by the player.
        pLoss: int, the total number of losses by the player.
        hand: list, the hand of cards held by the player.
        bet: int, the amount of the current bet.
        score: int, the player's score in the current game.

    Attributes:
        pid: int, sequential id number of the player.
        pUserName: str, the username of the player.
        moneyMade: int, the total money made by the player.
        moneyLost: int, the total money lost by the player.
        currentGame: str, the current game the player is playing.
        winCount: int, the total number of wins by the player.
        lossCount: int, the total number of losses by the player.
        hand: list, the hand of cards held by the player.
        bet: int, the amount of the current bet.
        score: int, the player's score in the current game.
        money: int, the current credit balance of the player.

    Raises:
        TypeError: if the credit is not an integer.
        ValueError: if the credit is not positive.
    """
    _pid = 1  # Class variable to assign sequential player IDs

    def __init__(self, pUserName="", pCredit=500, pMoneyMade=0, pMoneyLost=0,currGame="", pWin=0, pLoss=0, hand=[], bet=0, score=0):
        self._pUserName = pUserName
        self._moneyMade = pMoneyMade
        self._moneyLost = pMoneyLost
        self._currentGame = currGame
        self._winCount = pWin
        self._lossCount = pLoss
        self._hand = hand
        self._bet = bet
        self._score = score
        self._money = pCredit
        self._currGame = "Baccarat"
        self._hand_bet = None
        self._amount_bet = None

        if not isinstance(pCredit, int):
            raise TypeError('Credit must be an integer.')
        elif pCredit < 1:
            raise ValueError('Credit must be positive.')

        self._pid = Player._pid  # Assign the player ID
        Player._pid += 1  # Increment the player ID for the next instance

    @property
    def pid(self):
        """Get the player id."""
        return self._pid

    @property
    def pUserName(self):
        """Get the player username."""
        return self._pUserName

    @property
    def moneyMade(self):
        """Get the total money made by the player."""
        return self._moneyMade

    @property
    def moneyLost(self):
        """Get the total money lost by the player."""
        return self._moneyLost

    @property
    def currentGame(self):
        """Get the current game the player is playing."""
        return self._currentGame

    @property
    def winCount(self):
        """Get the total number of wins by the player."""
        return self._winCount

    @property
    def lossCount(self):
        """Get the total number of losses by the player."""
        return self._lossCount

    @property
    def hand(self):
        """Get the hand of cards held by the player."""
        return self._hand

    @hand.setter
    def hand(self, hand):
        self._hand = hand

    @property
    def bet(self):
        """Get the amount of the current bet."""
        return self._bet

    @bet.setter
    def bet(self, amount):
        if not isinstance(amount, int):
            raise TypeError('Bet amount must be an integer.')
        if amount < 1:
            raise ValueError('Bet amount must be positive.')
        if amount > self._money:
            raise ValueError('Bet amount exceeds available credit.')
        self._bet = amount

    @property
    def score(self):
        """Get the player's score in the current game."""
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def money(self):
        """Get the current credit balance of the player."""
        return self._money

    @money.setter
    def money(self, credit):
        if not isinstance(credit, int):
            raise TypeError('Credit must be an integer.')
        if credit < 1:
            raise ValueError('Credit must be positive.')
        self._money = credit

    @property
    def hand_bet(self):
        """Get the hand on which the bet was made."""
        return self._hand_bet

    @hand_bet.setter
    def hand_bet(self, hand):
        if hand not in ['player', 'banker', 'tie']:
            raise ValueError('Invalid hand.')
        self._hand_bet = hand

    @property
    def amount_bet(self):
        """Get the amount of a bet."""
        return self._amount_bet

    @amount_bet.setter
    def amount_bet(self, amount):
        if not isinstance(amount, int):
            raise TypeError('Amount must be an integer.')
        if amount < 1:
            raise ValueError('Amount must be positive.')
        if amount > self._money:
            raise ValueError('Amount exceeds available credit.')
        self._amount_bet = amount

    def is_valid_bet(self):
        """Checks if the current bet is valid."""
        if self._hand_bet not in ['player', 'banker', 'tie'] or self._amount_bet <= 0:
            return False
        return True

    def win(self):
        """Perform the necessary actions upon a player win: adds the winnings
        to the balance according to the bet and resets the bet.

        Raises:
            InvalidBet: If the player does not have a valid bet.
        """
        if self.is_valid_bet():
            if self._hand_bet == 'player':
                self._money += self._amount_bet
                self._moneyMade += self._amount_bet
                self._winCount += 1
            elif self._hand_bet == 'banker':
                self._money += int(self._amount_bet * 0.95)
                self._moneyMade += int(self._amount_bet * 0.95)
                self._winCount += 1
            elif self._hand_bet == 'tie':
                self._money += int(self._amount_bet * 8)
                self._moneyMade += int(self._amount_bet * 8)
                self._winCount += 1
            self._hand_bet = None
            self._amount_bet = 0
        else:
            raise InvalidBet('Player does not have a valid bet.')

    def lose(self):
        """Perform the necessary action upon a player loss: resets the bet.

        Raises:
            InvalidBet: If the player does not have a valid bet.
        """
        if self.is_valid_bet():
            self._moneyLost += self._amount_bet
            self._money -= self._amount_bet
            self._lossCount += 1
            self._hand_bet = None
            self._amount_bet = 0
        else:
            raise InvalidBet('Player does not have a valid bet.')

    def __repr__(self):
        """Return the representation string as if the object was
        called when creating a new instance with the current credit balance.
        """
        return f'Player(pCredit={self._money}, pUserName="{self._pUserName}", pMoneyMade={self._moneyMade}, pMoneyLost={self._moneyLost}, currGame="{self._currentGame}", pWin={self._winCount}, pLoss={self._lossCount}, hand={self._hand}, bet={self._bet}, score={self._score})'

    def __str__(self):
        """Return a string separated by new lines with the id, username, credit,
        amount, and bet of the player in case there is a valid one.
        """
        bet = f'Hand bet: {self._hand_bet}, Amount bet: {self._amount_bet}'
        no_bet = 'No bet'
        return f'Player: {self._pid}, Username: {self._pUserName}, Credit: {self._money}, {bet if self.is_valid_bet() else no_bet}.'
