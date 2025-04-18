import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_values = {
    "A" : 5,
    "B" : 7,
    "C" : 3,
    "D" : 9
}

def check_winnings(columns, lines, bet, values) :
    winnings = 0
    winning_lines = []
    for line in range(lines) :
        symbol = columns[0][line]
        for column in columns :
            symbols_to_check = column[line]
            if symbol != symbols_to_check :
                break
            else :
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
                
        return winnings,winning_lines
                
    

def get_slot_machine_spin(rows, cols, symbols) :
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns
    
def print_slot_machine(columns) :
    for row in range(len(columns[0])) :
        for i, column in enumerate(columns) :
            if i != len(columns) -1 :
                print(column[row], end =" | ")
            else : 
                print(column[row], end ="")
                
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? : $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                # print(f"You have deposited {amount}$")
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a digits only")
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            f"Enter the number of lines to bet on (1- {str(MAX_LINES)})? :")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print(f"Value must be between 1 - {str(MAX_LINES)}.")
        else:
            print("Please enter a digit only.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet? : $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= MIN_BET and amount <= MAX_BET:
                print("You bet so much money")
                break
            else:
                print(f"Please bet between {str(MIN_BET)} to {str(MAX_BET)}.")
        else:
            print("Please print digits only.")
    return amount

def spin(balance) :
    lines = get_number_of_lines()
    while True :
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}"
            )
        else:
            break
        
        print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()
