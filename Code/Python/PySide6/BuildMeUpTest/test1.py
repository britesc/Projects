#!/usr/bin/env python3
# coding: utf-8

import fnmatch
import os
import subprocess

    
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


class FindApps:
    
    def __init__(self):
        pass
    
    def __str__(self):
        return f"Find Applications"
    
    def getVersion():
        vVersion = "1.0.0"
        return vVersion

    def search():
        # Read the list of programs

        for dict_item in applicationsNeeded:
            vAppName = dict_item['AppName']
            vAppVerGet = dict_item['AppVerGet']
            vRegexStart = dict_item['RegexStart']            
            vRegexEnd = dict_item['RegexEnd']
                                   
            for root, dirnames, filenames in os.walk('/usr/bin'):
                for filename in fnmatch.filter(filenames, vAppName.lower()):
                    vPathJoin = os.path.join(root, filename)
                    vRequest = vPathJoin + " " + vAppVerGet
                    process = subprocess.run(vRequest, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    
                    responseVersion = process.stdout
                    if not responseVersion:
                        responseVersion = process.stderr
                    responseVersion = responseVersion.rstrip('\n')
                    found = responseVersion[vRegexStart:vRegexEnd]
                    
                    applicationsFound.append(
                        {
                            'app': vAppName,
                            'location':  vPathJoin,
                            'version': found 
                        }
                    )                                
        return None     



def main():
    FindApps.search()
    print(f'{applicationsFound}')
    

if __name__ == '__main__':
    main()
            