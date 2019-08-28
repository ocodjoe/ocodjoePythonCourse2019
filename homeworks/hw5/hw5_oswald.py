#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:01:54 2019

@author: oswaldcodjoe
"""
############
import os
os.getcwd() 
os.chdir('/Users/oswaldcodjoe/OneDrive - Washington University in St. Louis/Summer 19/Python/ocodjoePythonCourse2019/homeworks/hw5')
############

#establishing a class of nodes
class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
    def __str__(self):
        return str(self.value)
    
    
#Creating a linked list class
class LinkedList():
    def __init__(self, r = None):
        self.root = r
        self.size = 0
        
    def length(self):
        return self.size
    
    def addNode(self, new_value):
        new_node = Node(new_value, self.root)
        self.root = new_node
        self.size += 1
    
    def addNodeAfter(self, new_value, after_value):
        #cont. here...
        
    def addNodeBefore(self, new_value, before_value):
        #cont. here...
    
    def removeNode(self, node_to_remove):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                    self.size -= 1
                    return True
            else:
                prev_node = this_node 
                this_node = this_node.get_next()
                
        return False
    
    
    def removeNodesByValue(self, value):
        #cont. here...
        
    def reverse(self):
        new_linked_list = self.reverse()
        return new_linked_list
    
    
    def __str__(self):
        #cont. here..
        
    def hasCycle(self):
        #cont. hewre...
        
        
    
    
#creating nodes
nodeA = Node(5)
nodeB = Node(12)
nodeC = Node(9)
nodeD = Node(2)

#linking the nodes
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = 'na'

