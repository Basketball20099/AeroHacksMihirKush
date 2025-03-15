import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import simpledialog
from BankAccountApp import Banking

bank = Banking()

def update_textbox(message):
    command_textbox.insert(tk.END, message + "\n")
    command_textbox.yview(tk.END)

def create_account():
    account_type = simpledialog.askstring("Create Account", "Enter account type (savings/checking/business):")
    account_name = simpledialog.askstring("Create Account", "Enter account name:")
    balance = simpledialog.askfloat("Create Account", "Enter initial balance:")
    
    if account_type and account_name and balance is not None:
        bank.create_accounts(account_type.lower(), account_name, balance)
        update_textbox(f"✅ Account '{account_name}' ({account_type.capitalize()}) created successfully!")

def deposit():
    account_name = simpledialog.askstring("Deposit", "Enter account name:")
    amount = simpledialog.askfloat("Deposit", "Enter deposit amount:")
    
    if account_name and amount is not None:
        bank.deposit(account_name, amount)
        update_textbox(f"💰 Deposited ${amount:.2f} into '{account_name}'.")

def withdraw():
    account_name = simpledialog.askstring("Withdraw", "Enter account name:")
    amount = simpledialog.askfloat("Withdraw", "Enter withdrawal amount:")
    
    if account_name and amount is not None:
        bank.withdraw(account_name, amount)
        update_textbox(f"💸 Withdrew ${amount:.2f} from '{account_name}'.")

def check_balance():
    account_name = simpledialog.askstring("Check Balance", "Enter account name:")
    
    if account_name:
        account = bank.find_account(account_name)
        if account:
            update_textbox(f"📌 Balance for '{account_name}': ${account.balance:.2f}")
        else:
            update_textbox("❌ Account not found!")

def check_account_info():
    if not bank.accounts:
        update_textbox("❌ No accounts found!")
        return
    
    update_textbox("📜 All Accounts:")
    for account in bank.accounts:
        update_textbox(account.account_info())

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Banking System")
frame = tk.Frame(root)
frame.pack()

createacc_btn = tk.Button(frame, text="Create Account", command=create_account)
createacc_btn.pack()

depo_btn = tk.Button(frame, text="Deposit", command=deposit)
depo_btn.pack()

withdraw_btn = tk.Button(frame, text="Withdraw", command=withdraw)
withdraw_btn.pack()

check_btn = tk.Button(frame, text="Check Balance", command=check_balance)
check_btn.pack()

accinfo_btn = tk.Button(frame, text="Check Account Info", command=check_account_info)
accinfo_btn.pack()

exit_btn = tk.Button(frame, text="Exit", command=exit_app)
exit_btn.pack()

command_textbox = tksc.ScrolledText(root, height=10, width=50)
command_textbox.pack()

root.mainloop()
