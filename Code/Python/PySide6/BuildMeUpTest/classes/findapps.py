#!/usr/bin/env python3
# coding: utf-8

import os
import subprocess
import pprint

#import classes.variables as vMV
import variables as vMV
    
class FindApps:
    
    def __init__(self) -> None:
        pass
    
    
    def __repr__(self) -> str:
        return f'FindApps'
    
    def __str__(self) -> str:
       return f"Find Applications"
    
    
    def getVersion(self) -> str:
        vVersion = "1.0.0"
        return vVersion
    
    def appSearch(self) -> None:
        try:
            
            for dict_item in vMV.applicationsNeeded:
                vAppAlias = dict_item['AppAlias']
                vAppReal  = dict_item['AppReal']
                vAppVerGet = dict_item['AppVerGet']
                vRegexStart = dict_item['RegexStart']            
                vRegexEnd = dict_item['RegexEnd']
            
                request = "which " + vAppReal
                process = subprocess.run(request, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                
                vLocation = process.stdout  
                vLocation = vLocation.rstrip('\n')  

                vRequest = vLocation + " " + vAppVerGet
                process = subprocess.run(vRequest, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    
                responseVersion = process.stdout
                if not responseVersion:
                    responseVersion = process.stderr
                responseVersion = responseVersion.rstrip('\n')
                found = responseVersion[vRegexStart:vRegexEnd]
                                        
                                    
                vMV.applicationsFound.append(
                    {
                        'app': vAppAlias,
                        'alias': vAppReal,
                        'location':  vLocation,
                        'version': found 
                    }
                )                  
                        
            
        except:
            pass
            
            
        finally:        
            return None
   


def main():
    
    vFA = FindApps()
    vFA.appSearch()
    pprint.pprint(vMV.applicationsFound)


if __name__ == '__main__':
    main()
            