#!/usr/bin/env python3
# coding: utf-8

import fnmatch
import os
import subprocess
import classes.variables as miscVar
    
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

        for dict_item in miscVar.applicationsNeeded:
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
                    
                    miscVar.applicationsFound.append(
                        {
                            'app': vAppName,
                            'location':  vPathJoin,
                            'version': found 
                        }
                    )                                
        return None     



def main():
    FindApps.search()
    print(f'{miscVar.applicationsFound}')
    

if __name__ == '__main__':
    main()
            