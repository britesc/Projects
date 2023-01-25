#!/usr/bin/env python3
# coding: utf-8


import os
import sqlite3
from sqlite3 import Error
import classes.variables as miscVar



class DatabaseRoutines:


    def __init__(self):
        print(f"Init Method Called")

    def __enter__(self):
        print(f"Enter Method Called")
        return self

    def __exit__(self):
        if miscVar.vConnection:
            miscVar.vConnection.close()
        print(f"Exit Method Called")
   
    def __str__(self):
        return "SQLite3 Database Routines"
    
    def getVersion():
        vVersion = "Dev"
        return vVersion
    
    def getFunctions():
        vListOfFunctions = {
            "__init__       - pass",
            "__enter__      - Enter Function",
            "__exit__       - Close all connections",
            "__str__       - Return Overview of Class",
            "getFunctions   - Return List of Functions",
            "getVersion     - Return Class Version Number",
            "createDatabase - Create the SQLite Database",
            "dropDatabase   - Drop the SQLite Database",
            "createTables   - Create the Tables",
            "putProjectDir  - Store the Project Directory",
            "getProjectDir  - Retrieve the Project Directory"
        }
        return vListOfFunctions
    
    def connectDatabase(vDatabase):
        result = False
        try:
            vConnection = sqlite3.connect(vDatabase)
            result = True
  
        except Error as err:
            print('connectDatabase Query Failed: Error: %s' % (str(err)))
            result = False
            
        except Exception as err:
            print('connectDatabase Query Failed: Exception: %s' % (str(err)))
            result = False
 
        finally:    
            print(f"connectDatabase =  {vConnection}")
            vConnection.close()
#            time.sleep(1)
            return result
              
    
    def dropDatabase(vDatabase):
        result = False
        try: 
            if os.path.exists(vDatabase):
                os.remove(vDatabase)
                result = True
        
        except Error as err:
            print('dropDatabase Query Failed: Error: %s' % (str(err)))
            result = False
            
        except Exception as err:
            print('dropDatabase Query Failed: Exception: %s' % (str(err)))
            result = False
        
        finally:
            print(f"dropDatabase =  {result}")
 #           time.sleep(1)
            return result
    
    
    def createTables(vDatabase, vTable):
        result = False
        try:
            vConnection = sqlite3.connect(vDatabase)
            cursor = vConnection.cursor()
            cursor.execute(vTable)
            vConnection.commit()
            result = True
            print(f'{vTable}')
 
        except Error as err:
            print('createTables Query Failed: Error: %s' % (str(err)))
            result = False
            
        except Exception as err:
            print('createTables Query Failed: Exception: %s' % (str(err)))
            result = False
            
        finally:
            print(f"createTables =  {result}")            
            vConnection.close()
#            time.sleep(1)
            return result
            
    
    def putProjectDir(vDatabase, vQuery):
        result = False
        try:
            vConnection = sqlite3.connect(vDatabase)
            cursor = vConnection.cursor()
            cursor.execute(vQuery)
            vConnection.commit()
            result = True
            print(f'{vQuery}')
 
        except Error as err:
            print('putProjectDir Query Failed: Error: %s' % (str(err)))
            result = False
            
        except Exception as err:
            print('putProjectDir Query Failed: Exception: %s' % (str(err)))
            result = False
            
        finally:
            print(f"putProjectDir =  {result}") 
            vConnection.close()      
#            time.sleep(1)     
            return result
        
        
    
    def getProjectDir():
        pass
    

def main():
    DatabaseRoutines.connectDatabase(miscVar.vDatabase)
    DatabaseRoutines.createTables(miscVar.vDatabase,  miscVar.vTable1)
    DatabaseRoutines.putProjectDir(miscVar.vDatabase, miscVar.vTable1Delete)
    DatabaseRoutines.putProjectDir(miscVar.vDatabase, miscVar.vTable1Insert)
    

if __name__ == '__main__':
    main()
