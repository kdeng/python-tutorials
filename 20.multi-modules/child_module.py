"""
This is a child module with a global variable
"""

balance = 0

def change_it(n):
    global balance
    balance = n



def get_balance():
    return balance