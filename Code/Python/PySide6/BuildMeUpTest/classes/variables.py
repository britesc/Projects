#!/usr/bin/env python3
# coding: utf-8

vTestVar = "Hello There"

## This is a list of needed applications
#  It contains dictionaries

applicationsNeeded = [
    {
        "AppName": "Aspell",
        "AppVerGet": "-v",
        "RegexStart": 60,
        "RegexEnd": 66
    },  
    {
        "AppName": "Awk",
        "AppVerGet": "-W version",
        "RegexStart": 5,
        "RegexEnd": 10
    },       
    {
        "AppName": "Bash",
        "AppVerGet": "--version",
        "RegexStart": 17,
        "RegexEnd": 23
    },      {
        "AppName": "CMake",
        "AppVerGet": "--version",
        "RegexStart": 14,
        "RegexEnd": 20
    },
    {
        "AppName": "Dia",
        "AppVerGet": "-v",
        "RegexStart": 12,
        "RegexEnd": 18
    },
    {
        "AppName": "Dot",
        "AppVerGet": "-V",
        "RegexStart": 22,
        "RegexEnd": 29
    },
    {
        "AppName": "Doxygen",
        "AppVerGet": "--version",
        "RegexStart": 0,
        "RegexEnd": 5
    },
    {
        "AppName": "Git",
        "AppVerGet": "-v",
        "RegexStart": 12,
        "RegexEnd": 20
    },
    {
        "AppName": "GMake",
        "AppVerGet": "--version",
        "RegexStart": 8,
        "RegexEnd": 12
    },
    {
        "AppName": "Ninja",
        "AppVerGet": "--version",
        "RegexStart": 0,
        "RegexEnd": 6
    },
    {
        "AppName": "Pip3",
        "AppVerGet": "--version",
        "RegexStart": 4,
        "RegexEnd": 10
    },
    {
        "AppName": "Python3",
        "AppVerGet": "--version",
        "RegexStart": 7,
        "RegexEnd": 13
    },
    {
        "AppName": "Sed",
        "AppVerGet": "--version",
        "RegexStart": 23,
        "RegexEnd": 26
    },    {
        "AppName": "Whoami",
        "AppVerGet": "--version",
        "RegexStart": 23,
        "RegexEnd": 27
    }
]         


applicationsFound = []


def main():
    print("WARNING:")
    print("There is no executable code in this file.")
    print("It is used to store GLOBAL Variables and Constants")
    

if __name__ == '__main__':
    main()


