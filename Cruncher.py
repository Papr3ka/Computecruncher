# -*- coding: utf-8 -*-
# Copyright (c) 2019 Benjamin Yao
import math
import os
import platform
from decimal import *
from decimal import Decimal as dec
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
def wait():
    if waitsetc == 1:
        clear()
        wait = str(input("Press enter to continue..."))
    if waitsetc == 0:
        wait = str(input("Press enter to exit..."))
    clear()
def BBP_Pi():
    clear()
    x = 0
    pi = 0
    for x in range(0,maxpr): 
        pi += dec((dec(1) / dec(16) ** dec(x)) * (dec(4) / (dec(8) * x + dec(1)) - dec(2) / (dec(8) * x + dec(4)) - dec(1) / (dec(8) * x + dec(5)) - dec(1) / (dec(8) * x + dec(6))))
        print(pi)
    finalpi = dec(int(pi * dec(10 ** maxpr)) / dec(10 ** maxpr))
    clear()
    print("Done!\n")
    print(finalpi)
    if maxpr == 0:
        lensub = 0
    stlength = len(str(finalpi)) - lensub
    print("\nLength",stlength)
    if textfc == "Y" or textfc == "y":
        outFile = open("PI.txt", "w+")
        outFile.write(str(finalpi))
        outFile.close() 
def Euler():
    clear()
    x = 0
    euler = 0
    for x in range(0,maxpr):
        euler += dec(dec(1) / dec(math.factorial(int(x))))
        print(euler)
    finaleuler = dec(int(euler * dec(10 ** maxpr)) / dec(10 ** maxpr))
    clear()
    print("Done!\n")
    print(finaleuler)
    if maxpr == 0:
        lensub = 0
    stlength = len(str(finaleuler)) - lensub
    print("\nLength",stlength)
    if textfc == "Y" or textfc == "y":
        outFile = open("Euler.txt", "w+")
        outFile.write(str(finaleuler))
        outFile.close() 
def rootcrunch():
    root = dec(input("Root:"))
    x = dec(input("Root of:"))
    clear()
    print("Calculating")
    sq = dec(x ** dec(dec(1) / dec(root)))
    clear()
    print("Converting")
    finalsq = dec(int(sq * dec(10 ** maxpr)) / dec(10 ** maxpr))
    clear()
    print("Done!\n")
    print(finalsq)
    if finalsq - int(finalsq) != 0:
        sqvar = 1
    else:
        sqvar = 0
    stlength = len(str(finalsq)) - sqvar
    print("\nLength",stlength)
def Gratio():
    clear()
    print("Calculating")
    Golden = dec(dec(dec(1) + dec(dec(5) ** dec(0.5))) / dec(2))
    clear()
    print("Converting")
    finalgolden = dec(int(Golden * dec(10 ** maxpr)) / dec(10 ** maxpr))
    clear()
    print("Done!\n")
    print(finalgolden)
    if maxpr == 0:
        lensub = 0
    else:
        lensub = 1
    stlength = len(str(finalgolden)) - lensub
    print("\nLength",stlength)
textfc = "n"
waitsetc = 1
maxpr = 0
lensub = 2
clear()
print(r"Select Constant to compute")
print("1:PI\n2:Euler\n3:Root\n4:Golden Ratio")
option = int(input("Option:"))
clear()
if option < 5 and option > 0:
    maxpr = int(input("Accurate Precicion:"))
if option == 1 or option == 2:
    print(r"Output Text file Y/N")
    textfc = str(input())
    wait()
if option == 1:
    getcontext().prec = maxpr + 32
    BBP_Pi()
if option == 2:
    getcontext().prec = maxpr + 32
    Euler()
if option == 3:
    getcontext().prec = maxpr + 16
    rootcrunch()
if option == 4:
    getcontext().prec = maxpr + 8
    Gratio()
print("\nAccurate Precision",maxpr)
if option > 4 or option < 1:
    clear()
    print("Invalid Option")
if maxpr < 0:
    clear()
    print("Invalid Option")
waitsetc = 0
wait()
