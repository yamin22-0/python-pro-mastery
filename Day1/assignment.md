Day 1: Mini Wallet (M-Pesa lite)

Pure Python, no libraries, runs in the terminal.

First, write 5–8 lines on how you'll store users and transactions. Then build a program where:

A user has a phone number, a name, and a balance
You can register a user (no duplicate phone numbers)
You can deposit money (amount must be positive)
You can withdraw money, with a flat fee of 10 (the user needs balance plus fee)
You can send money to another registered user. The fee is 0 up to 100, 5 up to 500, 10 up to 1000, and 20 above that. The sender pays the fee.
You can't send to yourself or to an unregistered number
Every action is recorded, and you can print a mini-statement (last 5 transactions) for any user
Invalid input never crashes the program

Must pass: send 500 from a user with 505 (works, balance 0), send 500 from a user with 504 (rejected), withdraw exactly balance minus fee (works).

Warm-up: Two Sum. Solve it first the slow way, then with a dictionary.