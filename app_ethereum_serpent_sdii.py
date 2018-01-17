#!/usr/bin/env python
# An simple application that creates a token and perform
# transfers.
#
# Author: Mateus Sousa && Adriana Ribeiro (UFBA)
# January - 2018

from ethereum.tools import tester as t

c = t.Chain()
# t.STARTGAS

# Set gas price by transaction
t.GASPRICE = 100

# create a contract
x0 = c.contract("contract.se",language='serpent')
# Mining some blocks
c.mine(5)

x0.token(20000) # Initialize wallet
success = x0.transfer(t.a0,t.a1,500) # Transfer status

if success:
    print (x0.balanceOf(t.a1),x0.balanceOf(t.a0))
else:
    print ("Error on transaction!")
