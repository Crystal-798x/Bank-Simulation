# Crystal Bank Limited: a bank system simulation in Python

A command-line bank I built to learn Python. You can open an account, log in, deposit, withdraw, transfer money to another account, and view your transaction history. Everything is saved to a file, so your accounts are still there the next time you run it.

This is my first real Python project, so the code is plain and written by hand. No frameworks, no external libraries.

## What it does

- **Create an account:** enter a name and get a random 8-digit account number
- **Log in** with your account number
- **Deposit** and **withdraw**, with checks so you can't withdraw more than you have or enter zero, negative or non-numeric amounts
- **Transfer** to another account. It refuses transfers to a missing account, to yourself, or for more than your balance
- **History:** every deposit, withdrawal and transfer is recorded with a timestamp. Transfers are recorded in both accounts
- **Saving:** accounts are stored with `pickle` in `data.pkl` and loaded again on the next start

## How to run it

You need Python 3. Nothing else to install.

```
python main.py
```

On the first run there is no save file, so it starts with two demo accounts:

| Account number | Name        | Balance |
|----------------|-------------|---------|
| 22344322       | Abdul Salam | 30000   |
| 21344312       | Eshan       | 30000   |

Choose **A** to log in with one of those numbers, or **B** to create your own account. Choose **5** in the menu to exit, which is also when everything gets saved.

To reset the bank, delete `data.pkl`.

## How it works

All accounts live in one dictionary. The key is the account number, and the value is a list holding three things:

```
account number -> [name, balance, history]
```

The history is a dictionary of numbered records (`0, 1, 2, ...`), where record `0` is always "Account Created". Each new deposit, withdrawal or transfer gets the next number.

The functions are `deposit()`, `withdraw()`, `transfer()`, `history()` and `open_accoiunt()` (yes, that typo is in the code). A small helper formats the time for each record.

## What I learned building it

- Dictionaries are for finding things by a name or number, lists are for things in order, and nesting them gets confusing fast
- Two variable names can point at the same list, so changing one changes the other. This is why a deposit updates the account without writing anything back
- `try` and `except` for bad input, and that an `except` block does not stop the function by itself
- The difference between `return` and `sys.exit()`, and why exiting early can skip the save
- `input()` always gives text, so account numbers have to be converted before they match the dictionary keys
- Saving data with `pickle`, and why JSON turns number keys into text when you reload them
- Checking everything first and changing balances second, so a failed transfer never loses money

## Known limits and ideas for later

- No PIN or password. Anyone who knows an account number can log in
- Whole numbers only, no decimals, so it isn't a realistic money model
- History entries are plain sentences, not separate fields, so they can't be totalled or filtered
- The start menu runs once, so you restart the program to log in after creating an account
- Data is saved when you choose Exit, not after every action, so closing the window loses that session
- Ideas: frozen accounts, an automated simulation that creates random customers and transactions, and rewriting it with classes

## Why I built it

I wanted to understand how the pieces of a program fit together by building something with rules: money can't appear or vanish, and every change leaves a record. I wrote the code myself and used AI only to explain concepts and review my work.
