#!/usr/bin/env python3
# coding: utf-8

import fnmatch
import os
import subprocess
import re

    
## This is a list of needed applications
#  It contains dictionaries

applicationsNeededOld = [
    "Python3",
    "CMake",
    "Dot",
    "Dia",
    "Doxygen",
    "Ninja",
    "Git"    
    ]

applicationsNeeded = [
    {
        "AppName": "Python3",
        "AppVerGet": "--version",
        "AppRegex": "None"
    },
    {
        "AppName": "CMake",
        "AppVerGet": "--version",
        "AppRegex": "None"
    },
    {
        "AppName": "Dot",
        "AppVerGet": "-V",
        "AppRegex": "None"
    },
    {
        "AppName": "Dia",
        "AppVerGet": "-v",
        "AppRegex": "None"
    },
    {
        "AppName": "Doxygen",
        "AppVerGet": "--version",
        "AppRegex": "None"
    },
    {
        "AppName": "Ninja",
        "AppVerGet": "--version",
        "AppRegex": "None"
    },
    {
        "AppName": "Git",
        "AppVerGet": "-v",
        "AppRegex": "None"
    }    
]

applicationsFound = []


class FindApps:
    print("Checking for Files Required for the System")
    
    def __init__(self):
        pass
    
    def __str__(self):
        return f"Find Applications"
    

    def search():
        matches=[]
        # Read the list of programs

        for dict_item in applicationsNeeded:
            vAppName = dict_item['AppName']
            vAppVerGet = dict_item['AppVerGet']
            vAppRegex = dict_item['AppRegex']            
  
            #print(f'vAppName = {vAppName}')
            #print(f'vAppVerGet = {vAppVerGet}')
            #print(f'vAppRegex = {vAppRegex}')
                                   
            for root, dirnames, filenames in os.walk('/usr/bin'):
                for filename in fnmatch.filter(filenames, vAppName.lower()):
                    flute = os.path.join(root, filename)
                    request = flute + " " + vAppVerGet
                    process = subprocess.run(request, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    
                    responseVersion = process.stdout
                    if not responseVersion:
                        responseVersion = process.stderr
                    responseVersion = responseVersion.rstrip('\n')
                    str = responseVersion
                    try:
                        found = re.search('git version (.+?) ', str).group(1)
                        print(found)
                    except AttributeError:
                        pass
                    
                    applicationsFound.append(
                        {
                            'app': vAppName,
                            'location':  flute,
                            'version': responseVersion 
                        }
                    )                                
        print(f'Applications Found = {applicationsFound}')
        


"""git version 2.37.2
str = "123AAATorontoZZZ123"
try:
    found = re.search('git version (.+?) ', str).group(1)
    print(found)
except AttributeError:
    pass
"""
def main():
    FindApps.search()
    

if __name__ == '__main__':
    main()
            