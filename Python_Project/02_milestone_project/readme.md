# 🃏 War Card Game in Python

This project is a **simple implementation of the classic War Card Game** using **Python and Object-Oriented Programming (OOP)**.

It is designed for **beginners** to understand:

* Classes and Objects
* Lists
* Game logic
* Control flow
* Basic OOP concepts

---

## 📌 Game Rules (Simple Explanation)

1. A standard deck of **52 cards** is created.
2. The deck is **shuffled**.
3. Cards are **divided equally** between two players.
4. Each round:

   * Both players play **one card**.
   * The player with the **higher card value wins the round**.
   * The winner takes **both cards** and puts them at the bottom of their deck.
5. **WAR condition**:

   * If both cards have the **same value**, a WAR happens.
   * Each player puts **3 cards face down** into the war pile.
   * In the next round, new cards are compared.
   * The winner takes **all cards in the war pile**.
6. The game ends when a player has **no cards left**.

---

## 🧱 Project Structure

### 1️⃣ Card Class

Represents a single playing card.

**Attributes:**

* `suit` (Hearts, Diamonds, Spades, Clubs)
* `rank` (Two to Ace)
* `value` (numeric value of the rank)

**Special Method:**

* `__str__()` → returns card in readable format
  Example: `King of Hearts`

---

### 2️⃣ Deck Class

Represents a deck of 52 cards.

**Responsibilities:**

* Create all 52 cards
* Shuffle the deck
* Deal cards to players

**Important Methods:**

* `shuffle()` → shuffles the deck
* `pic_card()` → removes and returns one card from the deck

---

### 3️⃣ Player Class

Represents a player in the game.

**Attributes:**

* `name`
* `player_all_card` (list of cards the player has)

**Important Methods:**

* `remove_one_card()` → plays one card
* `add_card()` → adds one or multiple cards to the player
* `__str__()` → shows how many cards the player has

---

## ⚔️ WAR Logic (Important Part)

* When both players play cards with the **same value**:

  * The cards are added to a **war pile**.
  * Each player places **3 more cards** into the war pile.
  * The next round decides the winner.
* The winner of the WAR takes **all cards from the war pile**.
* If a player does not have enough cards during WAR, the **other player wins**.

---


## 🎯 Concepts Used

* Object-Oriented Programming (OOP)
* Classes and Objects
* Lists and List Operations
* Loops and Conditional Statements
* Game Logic Implementation

---

## 🚀 Future Improvements

## 🖥️ Sample Output

```
Prateek plays: King of Hearts
Yadav plays: King of Spades
⚔️ WAR! Same value!

Prateek plays: Ace of Diamonds
Yadav plays: Queen of Clubs
🏆 Prateek wins this round
```

---

