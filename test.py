#!/usr/bin/python
#import os
#import datetime
#import numpy
#import re
#import argparse

#1/11/2020 Update to Python 3

def isPalindrome(word):
    return word == word[::-1]

if __name__== "__main__":
    print(isPalindrome("mom"))
    print(isPalindrome("watermelon"))