# This is a program that simulates a mini ATM.
# @author Tyler Mowen

def main() :
    balance = 1500
    choice = "W"

    # While loop repeats until user enters 'E/e' for the
    # menu choice.
    while (choice != 'E') :
        
        choice = getMenuChoice()
        
        if (choice == 'W') :
            withdraw = float(input("Enter amout withdraw: $"))
            if (withdraw > balance) :
                print("Insufficient funds.")
            elif (withdraw > 0) :                    
                balance -= withdraw
                print(f"Please take your ${withdraw:,.2f}")
            else:
                print("Improper withdraw amount entered.")
        elif (choice == 'D') :
            deposit = float(input("Enter deposit amount: $ "))
            if (deposit > 0) : 
                balance += deposit
                print(f"${deposit:,.2f} deposited.")
            else:
                print("Improper deposit amount entered.")
        elif (choice == 'B') :
            print(f"Current balance: ${balance:,.2f}")
    print()
    print("Thank you for banking with us.")

# getMenuChoice presents a banking menu of choices.
# @return The customer's menu choice as a single upper
# case letter.
def getMenuChoice() :
    line = "=" * 20
    print()
    print(line)
    print("Enter W for Withdraw\nEnter D for Deposit\n" +
            "Enter B for Balance\nEnter E for Exit")
    print(line)
    choice = input("Choice: ")
 
    return choice.upper()
        

main() 