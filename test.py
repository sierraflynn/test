#!/usr/bin/python
#import os
#import datetime
#import numpy
#import re
#import argparse

#1/11/2020 Update to Python 3

def isAnagram(word):
    for i in range(len(word)):
        
        if(len(word) == 1):
            return True
        
        print(word[i] + ' ' + word[len(word)-1-i])
        print("Hi there")
        if word[i] != word[len(word)-1-i]:
            return False
        else:
            return True

if __name__== "__main__":
    print(isAnagram("mom"))