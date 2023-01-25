#!/usr/bin/env python3
# coding: utf-8

vTestVar = "Hello There"

## This is a list of needed applications
#  It contains dictionaries

applicationsNeeded = [
    {
        "AppAlias": "Aspell",
        "AppReal": "aspell",
        "AppVerGet": "-v",
        "RegexStart": 60,
        "RegexEnd": 66
    },  
    {
        "AppAlias": "Awk",
        "AppReal": "awk",
        "AppVerGet": "-W version",
        "RegexStart": 5,
        "RegexEnd": 10
    },       
    {
        "AppAlias": "Bash",
        "AppReal": "bash",
        "AppVerGet": "--version",
        "RegexStart": 17,
        "RegexEnd": 23
    },
    {
        "AppAlias": "CMake",
        "AppReal": "cmake",
        "AppVerGet": "--version",
        "RegexStart": 14,
        "RegexEnd": 20
    },
    {
        "AppAlias": "Dia",
        "AppReal": "dia",
        "AppVerGet": "-v",
        "RegexStart": 12,
        "RegexEnd": 18
    },
    {
        "AppAlias": "Dot",
        "AppReal": "dot",
        "AppVerGet": "-V",
        "RegexStart": 22,
        "RegexEnd": 29
    },
    {
        "AppAlias": "Doxygen",
        "AppReal": "doxygen",
        "AppVerGet": "--version",
        "RegexStart": 0,
        "RegexEnd": 5
    },
    {
        "AppAlias": "Gdb",
        "AppReal": "gdb",
        "AppVerGet": "--version",
        "RegexStart": 31,
        "RegexEnd": 35
    },
    {
        "AppAlias": "Git",
        "AppReal": "git",
        "AppVerGet": "-v",
        "RegexStart": 12,
        "RegexEnd": 20
    },
    {
        "AppAlias": "GMake",
        "AppReal": "gmake",
        "AppVerGet": "--version",
        "RegexStart": 8,
        "RegexEnd": 12
    },
    {
        "AppAlias": "Jq",
        "AppReal": "jq",
        "AppVerGet": "--version",
        "RegexStart": 3,
        "RegexEnd": 6
    },
    {
        "AppAlias": "Ninja",
        "AppReal": "ninja",
        "AppVerGet": "--version",
        "RegexStart": 0,
        "RegexEnd": 6
    },
    {
        "AppAlias": "Pip3",
        "AppReal": "pip3",
        "AppVerGet": "--version",
        "RegexStart": 4,
        "RegexEnd": 10
    },
    {
        "AppAlias": "Python3",
        "AppReal": "python3",
        "AppVerGet": "--version",
        "RegexStart": 7,
        "RegexEnd": 13
    },
    {
        "AppAlias": "Qt",
        "AppReal": "qtdesignstudio",
        "AppVerGet": "--version",
        "RegexStart": 35,
        "RegexEnd": 41
    },
    {
        "AppAlias": "Qt Creator",
        "AppReal": "qtcreator",
        "AppVerGet": "--version",
        "RegexStart": 11,
        "RegexEnd": 16
    },   
    {
        "AppAlias": "Qt Design Studio",
        "AppReal": "qtdesignstudio",
        "AppVerGet": "--version",
        "RegexStart": 17,
        "RegexEnd": 23
    },
    {
        "AppAlias": "Sed",
        "AppReal": "sed",
        "AppVerGet": "--version",
        "RegexStart": 23,
        "RegexEnd": 26
    },
    {
        "AppAlias": "VSCode",
        "AppReal": "code",
        "AppVerGet": "--version",
        "RegexStart": 0,
        "RegexEnd": 6
    },    
    {
        "AppAlias": "Whoami",
        "AppReal": "whoami",
        "AppVerGet": "--version",
        "RegexStart": 23,
        "RegexEnd": 27
    }
]         


applicationsFound = []

vDatabase = r"test2.db"
vTable1 = r"CREATE TABLE IF NOT EXISTS project_dir (rowid INTEGER PRIMARY KEY, project_dir text NOT NULL);"
vTable1Delete = r"DELETE FROM project_dir;"
vTable1Insert = r"INSERT INTO project_dir (project_dir) VALUES('Another Dir');" 
vTable2 = r"CREATE TABLE IF NOT EXISTS apps (rowid INTEGER PRIMARY KEY, app text NOT NULL, alias text NOT NULL, location text NOT NULL, version text NOT NULL);"

vConnection = None


def main():
    print("WARNING:")
    print("There is no executable code in this file.")
    print("It is used to store GLOBAL Variables and Constants")
    

if __name__ == '__main__':
    main()


