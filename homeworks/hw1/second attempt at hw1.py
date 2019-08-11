#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 21:59:02 2019

@author: oswaldcodjoe
"""

#start with an empty portfolio
class Portfolio:
    
    description = 'Financial Instrument' #applies to all components of portfolio
    
    Cash = []        #Creating an empty list for cash, mutualfunds, and stocks
    MutualFund = []
    Stock = []

    pass  #telling python that I'm not specifying any class attributes yet
    
    #The code below allows the user to add cash to his portfolio under 2 
    #condition. (i) when he has no cash to start with, and (ii) when he already
    #has some cash at the time of adding the new cash. 
    def addCash(self, amount):
        if len(self.Cash)==0:
            self.Cash.append(float(amount))
            return "You've added $%d. You now have $%d in cash." %(float(amount),float(amount))
        elif len(self.Cash)!=0:
            self.Cash[0] = float(self.Cash[0] + amount)
            return "You've added" + float(amount) + "You now have " + float(self.Cash[0]) + "in cash."
    
    
    #The code below allows the user to withdraw cash from his portfolio, taking
    #into account 4 different conditions. (i)when he has no cash to begin with,
    #(ii)when he has some cash and it's more than the amount he wants to withdraw,
    #(iii) when he has some cash and it's equal to the amount he wants to withdraw,
    #(iv) when he has some cash but it's less than the amount he wants to withdraw.    
    def withdrawCash(self, amount):
        if len(self.Cash) == 0:
            return "You don't have sufficient cash in your portfolio."
        elif len(self.Cash) != 0 and self.Cash[0] > int(amount):
            self.Cash[0] = float(self.Cash[0] - amount)
            return "You've withdrawn $%d. You now have $%d in cash." %(amount, self.Cash[0])
        elif len(self.Cash) !=0 and self.Cash[0] == int(amount):
            self.Cash[0] = float(self.Cash[0] - amount)
            return "You've withdrawn $%d. You now have $%d in cash." %(amount, self.Cash[0])
        elif self.Cash[0] < int(amount):
            return "You don't have sufficient cash in your portfolio."
    
    
    #The code below allows the user to buy stock when he has no stocks to
    #begin with. Then it subtracts the cost of the stocks from the user's
    #cash account.     
    def buyStock(self, share_qty, stock):
        if len(self.Stock) == 0:
            self.Stock.append([share_qty, stock.Symbol]) 
            self.Cash[0] = float(self.Cash[0] - (share_qty*stock.Price))
            return "You've bought %d shares of %s stock. And your cash balance is $%d." %(share_qty, stock.Symbol, self.Cash[0])
            
        #The code below does the same thing as the one immediately above it;
        #except that it takes into account three different situations. (i) When
        #the user has some stocks to start with and more cash than the cost of
        #the stocks. (ii) When the user has some stocks to start with and a
        #cash amount that's equal to the cost of the stocks. (iii)When the user
        #has some stocks to start with but a cash amount less than the cost of
        #the stocks. 
        elif len(self.Stock) !=0 and self.Cash[0] > int(share_qty*stock.Price):
            self.Stock.append([int(share_qty), stock.Symbol])
            self.Cash[0] = float(self.Cash[0] - (share_qty*stock.Price))
            return "You've bought %d shares of %s stock. And your cash balance is $%d" %(share_qty, stock.Symbol, self.Cash[0])
        elif len(self.Stock) !=0 and self.Cash[0] == int(share_qty*stock.Price):
            self.Stock.append([int(share_qty), stock.Symbol])
            self.Cash[0] = float(self.Cash[0] - (share_qty*stock.Price))
            return "You've bought %d shares of %s stock. and your cash balance is $%d." %(share_qty, stock.Symbol, self.Cash[0]) 
        elif len(self.Stock) != 0 and self.Cash[0] < int(share_qty*stock.Price):
            return "You don't have sufficient funds to buy this stock."
   
    
    #The code below make it impossible to sell stocks if he has no stocks even of
    #some other kind.
    def sellStock(self, symbol, share_qty):
        if len(self.Stock) == 0:
            return "You don't have sufficient stocks to sell."
        
        #The code below allows user to sell stocks, indicate in his collection of 
        #stocks what he has sold, add the revenue from the sale to his cash balance.
        #And this is in the case when he has 0 cash at the time of the sale.
        elif len(self.Stock) != 0 and len(self.Cash)== 0:
            self.Stock.append([-int(share_qty),symbol])
            allowable_stocks = ["HFH"]
            price_of_allowables = [20]
            for i in allowable_stocks:
                if symbol == i:
                    self.Cash.append(-int(share_qty*price_of_allowables[0]))
                    return "You've sold %d shares of %s. And your cash balance is $%d." %(share_qty, symbol, self.Cash)
        
        #The code below does the same thing as the one immediately above it; except
        #that it is executed when there's already some money in the user's cash 
        #account. 
        elif len(self.Stock)!= 0 and len(self.Cash) != 0:    
            self.Stock.append([-int(share_qty),symbol])
            allowable_stocks = ["HFH"]
            price_of_allowables = [20]
            for i in allowable_stocks:
                if symbol == i:
                    self.Cash[0] = float(self.Cash[0]+ (share_qty*price_of_allowables[0]))
                    return "You've sold %d of %s stock. And your cash balance is %d." %(share_qty, symbol, self.Cash[0])
                    
        #The code below makes it impossible for user to sell more stocks than he
        #has in his collection of stocks. 
        #elif CONT. HERE
        
    
    #def buyMutualFund(self, share_qty, mutualfund):
        #if len(self.MutualFund) == 0:
            #self.MutualFund.append([share_qty,mutualfund.Symbol])
            #self.Cash[0] = self.Cash[0] - int() #cont. here cue from buystock
        #return "You've bought %d shares of %s." %(share_qty, mutualfund)
        
    def sellMutualFund(self, shares_qty, mutualfund):
        return "You've sold %d share of %s." %(share_qty, mutualfund)
    
    def print(self):
        return {"Cash":self.Cash, "Stocks":self.Stock, "MutualFund":self.MutualFund}
        #think of a way of presenting how many stocks and mutual funds are in 
        #the portfolio -- not just the history. 
        
    def history(self): 
        return {"Cash":self.Cash, "Stocks":self.Stock, "MutualFund":self.MutualFund}        
    


class Stock:
    
    description = 'Financial Instrument'
    
    def __init__(self, Price, Symbol):
        self.Price = Price
        self.Symbol = Symbol
            
class MutualFund:
    
    description = 'Financial Instrument'
    
    def __init__(self, Symbol):
        self.Symbol = Symbol 
        

s = Stock(20, "HFH")             #creating stock and 2 mutual funds
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")    
        
pfA = Portfolio()
pfA.addCash(100.50)
pfA.withdrawCash(300.5)
pfA.buyStock(5,s)
pfA.buyStock(5,s)
pfA.Stock
pfA.sellStock('HFH',1)  #cont. here..
pfA.Cash
pfA.sellStock(2,s)

pfA.print()
s.description
