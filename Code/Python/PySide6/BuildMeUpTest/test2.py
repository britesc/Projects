#!/usr/bin/env python3
# coding: utf-8


import os
import sqlite3
from sqlite3 import Error

vDatabase = r"test2.db"
vTable1 = """ CREATE TABLE IF NOT EXISTS project_dir (
            id integer PRIMARY KEY,
            project_dir text NOT NULL
        ); """

vConnection = None

class DatabaseRoutines:


    def __init__(self):
        print(f"Init Method Called")

    def __enter__(self):
        print(f"Enter Method Called")
        return self

    def __exit__(self):
        if vConnection:
            vConnection.close()
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
#        vConnection = None
        try:
            vConnection = sqlite3.connect(vDatabase)
            os.chmod(vDatabase, 0o777)
  
        except Error as err:
            print('connectDatabase Query Failed: Error: %s' % (str(err)))
            vConnection = None
            
        except Exception as err:
            print('connectDatabase Query Failed: Exception: %s' % (str(err)))
            vConnection = None
 
        finally:    
            print(f"connectDatabase =  {vConnection}")
            return vConnection
              
    
    def dropDatabase():
        result = False
        try: 
            if vConnection:
                vConnection.close()
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
            return result
    
    
    def createTables(vConnection, vTable):
        result = False
        try:
            cursor = vConnection.cursor()
            cursor.execute(vTable)
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
            return result
  
            
            
    
    def putProjectDir():
        pass
    
    def getProjectDir():
        pass
    

def main():
    vConnection = DatabaseRoutines.connectDatabase(vDatabase)
    DatabaseRoutines.createTables(vConnection,  vTable1)
    

if __name__ == '__main__':
    main()
