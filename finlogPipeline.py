'''🏗️ The Project Blueprint: "FinLog Engine"
You are building a backend processing script for a fintech asset management application. The data stream drops a messy list of log records containing transactions.

Your Pipeline Requirements:
The Data Cleaner (Functions & Loops): Write a function to filter out broken strings from the input data stream.

The Account Manager (OOP): Build a class that takes the clean data to manage a user's running asset balance.

The Pipeline Orchestrator: Write the execution code that passes data from the raw stream, through the function, and directly feeds it into your class objects.'''

# Raw dataset stream from server log
raw_log_stream = [5000.0, "NULL", 2500.50, "MISSING", -1200.00, 3100.25, "NULL", -450.00]
def sanitize_stream(raw_list):
    sanitized = []
    for i in raw_list:
        if i in ['MISSING','NULL']:
            continue
        sanitized.append(i)
    return sanitized


    

class UserPortfolio():
    def __init__(self,username,balance = 0.0):
        self.username = username
        self.balance = balance

    def process_transaction_history(self,transaction_list):
        for amount in transaction_list:

            self.balance += amount

    def display_status(self):
        print(f"{self.username} your final balance is {self.balance:.2f}")

clean_data = sanitize_stream(raw_log_stream)
my_portfolio = UserPortfolio("chika_excel")

my_portfolio.process_transaction_history(clean_data)
my_portfolio.display_status()