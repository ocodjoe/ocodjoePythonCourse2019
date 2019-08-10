#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:25:30 2019

@author: oswaldcodjoe
"""

##So I'm creating 3 classes/modeling 3 things: Portfolio, Stock, and MutualFund.
#Portfolio will be the main class and Cash(maybe), Stock, and MutualFund subclasses.

##Portfolio is defined to the following attributes: Cash, Stock, and Mutual Fund

##Portfolio has the following methods to 'manage/manipulate' its instances:
#addCash(amount) to add cash to it, buyStock(quantity_of_shares, name_of_stock),
#buyMutualFund(quantity_of_shares, name_of_mutualfund), sellStock(quantity_of_
#shares, name_of_stock), sellMutualFund(quantity_of_shares, name_of_mutualfund),
#withdrawCash(amount), history() to print all transactions in order ot time.

##Stock is defined to the following attributes: Price, and Symbol

##Mutual Fund is defined to the following attributes: Symbol 

###-----------------------------------------------------------------------

class Portfolio:
    def __init__(self, Cash, Stock, MutualFund):
        Cash = Cash
        Stock = Stock
        MutualFund = MutualFund
        
    def addCash(self, amount):
        
    def buyStock(self, number_of_shares, name_of_stock):
        
    def buyMutualFund(self, number_of_shares, name_of_mutualfund):
        
    def sellStock(self, number_of_shares, name_of_mutualfund):
        
    def sellMutualFund(self, number_of_shares, name_of_mutualfund):
    
    def withdrawCash(self, amount):
        
    def history(self):
        
        
    class Stock: 
        def __init__(self, Price, Symbol):
            Price = Price
            Symbol = Symbol
            
    class MutualFund:
        def __init__(self, Symbol):
            Symbol = Symbol
            
            
            
###My quick insights from videos so far:
    #A class can consist of variables too, not just functions.
            
            
            
            