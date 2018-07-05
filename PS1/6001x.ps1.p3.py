#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 15:57:52 2018

@author: macintosh

Problem Set 1 - Problem 3
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

s = 'azcbobobegghakl'

count = 1
n = 1
m = 0
long = 1
ans = s[0]
y = len(s) - 1
start = 0
x = True


for i in range (y + 1):
                
    if s[m] <= s[n]:
        while x == True:
            start = m
            x = False     
        if m < y:
            m += 1
            count += 1
        if n < y:
            n += 1
        
          
    elif long  < count:
        long = count
        ans = s[start:n]
        start = 0
        x = True
        count = 1
        if m < y:
            m += 1
        if n < y:
            n += 1 
          
    elif long >= count:
            start = 0
            x = True
            if m < y:
                m += 1
            if n < y:
                n += 1
            count = 1

if long  < count:
        ans = s[start:]
        
       

print ("Longest substring in alphabetical order is:", ans)