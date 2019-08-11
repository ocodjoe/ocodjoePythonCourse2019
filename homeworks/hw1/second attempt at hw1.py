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
    def sellStock(self, symbol, share_qty):
        if len(self.Stock) == 0:
            return "You don't have sufficient stocks to sell."
        
        elif len(self.Stock) != 0 and len(self.Cash)== 0:
            self.Stock.append([-int(share_qty),symbol])
            allowable_stocks = ["HFH"]
            price_of_allowables = [20]
            for i in allowable_stocks:
                if symbol == i:
                    self.Cash.append(-int(share_qty*price_of_allowables[0]))
                    return "You've sold %d shares of %s. And your cash balance is $%d." %(share_qty, symbol, self.Cash)
                    
        elif len(self.Stock)!= 0 and len(self.Cash) != 0:    
            self.Stock.append([-int(share_qty),symbol])
            allowable_stocks = ["HFH"]
            price_of_allowables = [20]
            for i in allowable_stocks:
                if symbol == i:
                    self.Cash[0] = self.Cash[0]+ int(share_qty*price_of_allowables[0])
                    return "You've sold %d of %s stock. And your cash balance is %d." %(share_qty, symbol, self.Cash[0])
                    #and your stock transaction history is ...where - number means selling and positive means buying.
                #think of displaying stock operations by displaying self.Stock
        
        #I need to add one final bit to ensure that user can't sell more than what he has
        #the first if takes care of that in some way but only for empty stocks.

        
        
    
    def buyMutualFund(self, share_qty, mutualfund):
        return "You've bought %d shares of %s." %(share_qty, mutualfund)
        
    def sellMutualFund(self, shares_qty, mutualfund):
        return "You've sold %d share of %s." %(share_qty, mutualfund)
    
    def print(self):
        return {"Cash":self.Cash, "Stocks":self.Stock, "MutualFund":self.MutualFund}
        #think of a way of 
        
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
pfA.sellStock('HFH',1)  #cont. here..
pfA.Cash
pfA.sellStock(2,s)

pfA.print()
