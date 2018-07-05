#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 15:51:28 2018

@author: macintosh

Problem Set 1 - Problem 2
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print:

Number of times bob occurs is: 2
"""
s = 'azcbobobegghakl'
pattern = 'bob'
count = 0
flag = True
start = 0
while flag:
    a = s.find(pattern, start)
    
    if a == -1:
        flag = False
    else:
        count+=1
        start=a+1

print("Number of times bob occurs is:", count)
