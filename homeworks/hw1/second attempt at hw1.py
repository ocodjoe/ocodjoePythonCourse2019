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
    Cash_track =[]

    pass  #telling python that I'm not specifying any class attributes yet
    
    #The code below allows the user to add cash to his portfolio under 2 
    #condition. (i) when he has no cash to start with, and (ii) when he already
    #has some cash at the time of adding the new cash. 
    def addCash(self, amount):
        if len(self.Cash)==0:
            self.Cash.append(float(amount))
            self.Cash_track.append(float(amount))
            return "You've added $%d. You now have $%d in cash." %(float(amount),float(amount))
        elif len(self.Cash)!=0:
            self.Cash[0] = float(self.Cash[0] + amount)
            self.Cash_track.append(float(amount))
            return "You've added $%d. You now have $%d in cash" %(float(amount),float(self.Cash[0]))
    
    
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
            self.Cash_track.append(float(-amount))
            return "You've withdrawn $%d. You now have $%d in cash." %(amount, self.Cash[0])
        elif len(self.Cash) !=0 and self.Cash[0] == int(amount):
            self.Cash[0] = float(self.Cash[0] - amount)
            self.Cash_track.append(float(-amount))
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
            self.Cash_track.append(-float(share_qty*stock.Price))
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
            self.Cash_track.append(-float(share_qty*stock.Price))
            return "You've bought %d shares of %s stock. And your cash balance is $%d" %(share_qty, stock.Symbol, self.Cash[0])
        elif len(self.Stock) !=0 and self.Cash[0] == int(share_qty*stock.Price):
            self.Stock.append([int(share_qty), stock.Symbol])
            self.Cash[0] = float(self.Cash[0] - (share_qty*stock.Price))
            self.Cash_track.append(-float(share_qty*stock.Price))
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
                    self.Cash_track.append(float(share_qty*price_of_allowables[0]))
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
                    self.Cash_track.append(float(share_qty*price_of_allowables[0]))
                    return "You've sold %d of %s stock. And your cash balance is %d." %(share_qty, symbol, self.Cash[0])
                    
        #Note: Try to write code that makes it impossible for user to sell 
        #more stocks than he has in his collection of stocks. 
        #elif CONT. HERE. 
    
        
    #The code below allows the user to buy shares of mutual funds under certain
    #conditions. (i) if he has no cash to start with, he can't make a purchase, 
    #(ii)if he has some cash and it's greater than the cost of the mutual funds,
    #he can make a purchase, (iii) if he has some cash but it's less than the cost
    #of the mutual funds, he can't make a purchase. 
    def buyMutualFund(self, share_qty, mutualfund): 
        if len(self.Cash) == 0:
            return "You don't have sufficient funds to make the purchase."
        elif len(self.Cash) !=0 and self.Cash[0] > float(share_qty):
            self.MutualFund.append([float(share_qty),mutualfund.Symbol])
            self.Cash[0] = float(self.Cash[0] - float(share_qty))
            self.Cash_track.append(-float(share_qty))
            return "You've bought %s shares of %s. Your cas bal. is $%d." %(float(share_qty),mutualfund.Symbol,self.Cash[0])
        elif self.Cash[0] < float(share_qty) and len(self.Cash) !=0:
            return "You don't have sufficient funds to make the purchase."
        
     
    #cont. here...   
    def sellMutualFund(self, share_qty, mutualfund):
        return "You've sold %d share of %s." %(share_qty, mutualfund)
    
    #The code below returns the user's outstanding cash balance as well as
    #his the stocks and mutual funds in his portfolio. 
    def print(self):
        return {"Cash":self.Cash, "Stocks":self.Stock, "MutualFund":self.MutualFund}
           
    
    #The code below displays history of transactions by the user.
    def history(self): 
        return {"Cash":self.Cash_track, "Stocks":self.Stock, "MutualFund":self.MutualFund}        


#The code below allows the user to create stock objects.
class Stock:     
    
    description = 'Financial Instrument'
    
    def __init__(self, Price, Symbol):
        self.Price = Price
        self.Symbol = Symbol

#The code below allows the user to create mutualfund objects.            
class MutualFund:   
    
    description = 'Financial Instrument'
    
    def __init__(self, Symbol):
        self.Symbol = Symbol 
        
#The codes below are for testing the various sections of the software. 
s = Stock(20, "HFH")             
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")    
        
pfA = Portfolio()
pfA.addCash(100.50) 
pfA.withdrawCash(50)
pfA.buyStock(5,s)
pfA.Stock
pfA.sellStock('HFH',1)
pfA.Cash 
pfA.Cash_track 
pfA.sellStock(2,s)

pfA.buyMutualFund(10.3, mf1) 
pfA.MutualFund

pfA.print()    
pfA.history()

mf1.Symbol   

