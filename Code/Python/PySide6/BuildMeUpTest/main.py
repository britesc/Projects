#!/usr/bin/env python3
# coding: utf-8

#from misc import variables
import os
import sys
from classes.findapps import FindApps
import classes.variables as miscVar
from classes.databaseroutines import DatabaseRoutines 


def main():
    version = FindApps.getVersion()
    version2 = DatabaseRoutines.getVersion()

    print(version)
    print(version2)
    print(miscVar.vTestVar)
    print(sys.path)
    print(os.path.abspath("which"))

if __name__ == '__main__':
    main()