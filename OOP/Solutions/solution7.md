# Solution 7: Deck of Cards

## Approach Explanation
Card has suit and rank. Deck initializes all 52 and supports shuffle/deal.

## Step-by-Step Logic
1. Card class with suit and rank.
2. Deck creates all 52 cards.
3. shuffle uses random.shuffle, deal pops cards.

## Complexity
- **Time Complexity:** O(N) for shuffle
- **Space Complexity:** O(N)

## Code
```python
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __repr__(self): return f'{self.rank} of {self.suit}'

class Deck:
    suits = ['Hearts','Diamonds','Clubs','Spades']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    def __init__(self):
        self.cards = [Card(s,r) for s in self.suits for r in self.ranks]
    def shuffle(self): random.shuffle(self.cards)
    def deal(self, n=1): return [self.cards.pop() for _ in range(min(n, len(self.cards)))]
```
