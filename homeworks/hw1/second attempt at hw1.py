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
        
    def buyStock(self, share_qty, stock):    #this is when nothing exists.
        if len(self.Stock) == 0:
            self.Stock.append(share_qty)
            self.Stock.append(stock.Symbol)
            
        #cont. here:trying to account for if it already exists and if it doens't    
        elif len(self.Stock) !=0 and self.Cash[0] > int(share_qty*stock.Price):
            self.Stock[0] = self.Stock[0] + int(share_qty)
            self.Stock[1]
            self.Cash[0] = self.Cash[0] - int(share_qty*stock.Price)
            return "You've bought %d shares of %s stock. and your cash balance is %d" %(share_qty, stock.Symbol, self.Cash[0]) 
        elif len(self.Stock) != 0 and self.Cash[0] < int(share_qty*stock.Price):
            return "You don't have sufficient funds to buy this stock."
   
    #cont. here. Account     
    def sellStock(self, share_qty, stock):
        if stock.Symbol == self.Stock[1]:
            return self.Stock[0]- share_qty
        elif self.Stock[0] < share_qty:   
            return "You don't have sufficient stocks to sell."
    
            
    


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



pfA.sellStock(2,s)

