#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 21:59:02 2019

@author: oswaldcodjoe
"""

#start with an empty portfolio
class Portfolio:
    
    description = 'Financial Instrument' #applies to all components of portfolio
    
    Cash = []           #Creating variables within the class.
    MutualFund = []
    Stock = []
    

    pass  #telling python that I'm not specifying any class attributes yet
    
    #Done
    def addCash(self, amount):
        if len(self.Cash)==0:
            self.Cash.append(amount)
            return "You've added $%d. You now have $%d in cash." %(amount,amount)
        elif len(self.Cash)!=0:
            self.Cash[0] = self.Cash[0] + int(amount)
            return "You've added $%d. You now have $%d in cash." %(amount,self.Cash[0])
    #Done    
    def withdrawCash(self, amount):
        if len(self.Cash) == 0:
            return "You don't have sufficient cash in your portfolio."
        elif len(self.Cash) != 0 and self.Cash[0] > int(amount):
            self.Cash[0] = self.Cash[0] - int(amount)
            return "You've withdrawn $%d. You now have $%d in cash." %(amount, self.Cash[0])
        elif len(self.Cash) !=0 and self.Cash[0] == int(amount):
            self.Cash[0] = self.Cash[0] - int(amount)
            return "You've withdrawn $%d. You now have $%d in cash." %(amount, self.Cash[0])
        elif self.Cash[0] < int(amount):
            return "You don't have sufficient cash in your portfolio."
    #Done    
    def buyStock(self, share_qty, stock):    #this is when nothing exists.
        if len(self.Stock) == 0:
            self.Stock.append([share_qty, stock.Symbol]) 
            self.Cash[0] = self.Cash[0] - int(share_qty*stock.Price)
            return "You've bought %d shares of %s stock. And your cash balance is $%d." %(share_qty, stock.Symbol, self.Cash[0])
            
        #this accounts for special cases.    
        elif len(self.Stock) !=0 and self.Cash[0] > int(share_qty*stock.Price):
            self.Stock.append([int(share_qty), stock.Symbol])
            self.Cash[0] = self.Cash[0] - int(share_qty*stock.Price)
            return "You've bought %d shares of %s stock. And your cash balance is $%d" %(share_qty, stock.Symbol, self.Cash[0])
        elif len(self.Stock) !=0 and self.Cash[0] == int(share_qty*stock.Price):
            self.Stock.append([int(share_qty), stock.Symbol])
            self.Cash[0] = self.Cash[0] - int(share_qty*stock.Price)
            return "You've bought %d shares of %s stock. and your cash balance is $%d." %(share_qty, stock.Symbol, self.Cash[0]) 
        elif len(self.Stock) != 0 and self.Cash[0] < int(share_qty*stock.Price):
            return "You don't have sufficient funds to buy this stock."
   
    #cont. here. -- thus 4 more functions to go. before that add commoents to above done.    
    def sellStock(self, share_qty, stock):
        if stock.Symbol == self.Stock[1]:
            return self.Stock[0]- share_qty
        elif self.Stock[0] < share_qty:   
            return "You don't have sufficient stocks to sell."
    
    def buyMutualFund(self, share_qty, mutualfund):
        return "You've bought %d shares of %s." %(share_qty, mutualfund)
        
    def sellMutualFund(self, shares_qty, mutualfund):
        return "You've sold %d share of %s." %(share_qty, mutualfund)
    
    def print(self):
        return self.database
        
    def history(self): 
        return "You've conducted %s so far." %(self)        
    


class Stock:
    def __init__(self, Price, Symbol):
        self.Price = Price
        self.Symbol = Symbol
            
class MutualFund:
    def __init__(self, Symbol):
        self.Symbol = Symbol 
        

s = Stock(20, "HFH")             #creating stock and 2 mutual funds
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")    
        
pfA = Portfolio()
pfA.addCash(120)
pfA.buyStock(5,s)
pfA.buyStock(5,s)
pfA.Stock

pfA.sellStock(2,s)

