# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 2022

@author: ahmadalabassy
"""

import math

class Category:
    def __init__(self, category):
        self.name = category
        self.ledger = []

    def __str__(self):
        output = '{:*^30}'.format(f'{self.name}') + '\n'
        for item in self.ledger:
            output += '{:<23}'.format(item.get('description')[:23]) + '{:>7.2f}'.format(item.get('amount')) + '\n'
        output += 'Total: ' + str(self.get_balance())
        return output

    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": round(amount, 2), "description": description})

    def withdraw(self, amount, description = ''):
        if not self.check_funds(amount): return False
        self.ledger.append({"amount": round(-amount, 2), "description": description})
        return True

    def get_balance(self):
        return sum(item.get('amount') for item in self.ledger)

    def transfer(self, amount, category):
        status = self.withdraw(amount, f'Transfer to {category.name}')
        if status: category.deposit(amount, f'Transfer from {self.name}')
        return status

    def check_funds(self, amount):
        balance = self.get_balance()
        return bool(balance > amount or math.isclose(balance, round(amount, 2)))


def create_spend_chart(categories):
    # preparing data for print
    items, total  = [], 0
    for category in categories:
        expenditure = -sum((transaction.get('amount') for transaction in category.ledger if transaction.get('amount') < 0))
        items.append((expenditure, category.name.capitalize()))
        total += expenditure
    total = round(total, 2)

    # calculating percentages
    items = [(int(amount/total*10) * 10, category) for amount, category in items]
    # stretch goal: sorting descendingly
    # items = sorted([(int(round(amount/total*10) * 10), category) for amount, category in items] , reverse=True)
    
    # printing table
    output = 'Percentage spent by category\n'
    for y_step in range(100,-1,-10):
        # y-axis
        output += '{:>3}'.format(y_step) + '| '
        # plot points for chart
        for item in items:
            output += ('o  ' if item[0] >= y_step else '   ')
        output += '\n'
    # x-axis
    output += '    -'
    for item in items:
        output += '---'
    output += '\n'
    # x-axis labels
    length = max(len(category) for amount, category in items)
    for index in range(length):
        output += '     '
        for item in items:
            output += (f'{item[1][index]}  ' if index < len(item[1]) else '   ')
        if not index == length - 1: output += '\n'
    
    return output