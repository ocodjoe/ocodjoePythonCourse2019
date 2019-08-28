#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:19:55 2019

@author: oswaldcodjoe
"""

class Node:
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next
    def __str__(self):
        return str(self.value)
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self, value=None):
        node = Node(value)
        self.head = node  
        
    def addNode(self, new_value):
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.next is None:
                current.set_next(new_node)
                break
            else:
                current = current.get_next()
    
    def print_list(self):
        current = self.head
        while current:
            print(current.get_value())
            current = current.get_next()
    
    def length(self):  #cont. here..
        current = self.head
        total = 0
        while current:
            if current.next is None:
                total = total + 1
                return total
            

            
    


#This is for testing the LinkedList class
list1 = LinkedList(5)
list1.addNode(12)
list1.addNode(2)
list1.print_list()
list1.addNode(12)

list1.length()

        