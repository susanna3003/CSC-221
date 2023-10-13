# for when user chooses to manipulate CSV file

import pandas as pd

csvDF = pd.read_csv('M2Pro_CSV.csv')
excelDF = pd.read_excel('M2Pro_Excel.xlsx')
colNames = list(excelDF.columns)
rowNames = list(excelDF.index)

def userAction():
    # determine what action user would like to perform on file
    print("\nWays to manipulate this file:")
    print("1. Delete column(s)")
    print("2. Delete row(s)")
    print("3. Delete both")
    action = int(input("What action would you like to perform? "))
    return action

def delCols(csvDF):
    '''
    edited file with deleted cols
    '''
    print("You chose delete column(s)")
    print("Columns to delete: ")
    for i in range(len(colNames)):
        print(i, "\t", colNames[i])
       
    numToDel = int(input("How many columns would you like to delete? ")) 
       
    for i in range(numToDel):
        
        colIndex = int(input("Column number you wish to delete: "))
        toDel = colNames[colIndex]
        csvDF = csvDF.drop([toDel], axis=1)
    
    return csvDF

def delRows(csvDF):
    '''
    edited file with deleted rows
    '''
    print("You chose delete row(s)")
    print("Rows to delete: ")
    for i in range(len(rowNames)):
        print(i)
       
    numToDel = int(input("How many rows would you like to delete? ")) 
       
    for i in range(numToDel):
        
        rowIndex = int(input("Row number you wish to delete: "))
        csvDF = csvDF.drop(csvDF.iloc[rowIndex].name, inplace = True)
    
    return csvDF
    
    
def delBoth(csvDF):
    '''
    edited file with both deleted cols and rows
    '''
    print("You chose to delete both. Let's start with columns first.")
    print("Columns to delete: ")
    for i in range(len(colNames)):
        print(i, "\t", colNames[i])
       
    numToDel = int(input("How many columns would you like to delete? ")) 
       
    for i in range(numToDel):
        
        colIndex = int(input("Column number you wish to delete: "))
        toDel = colNames[colIndex]
        csvDF = csvDF.drop([toDel], axis=1)
        
    print("Rows to delete: ")  
    for i in range(len(rowNames)):
        print(i)
       
    numToDel = int(input("How many rows would you like to delete? ")) 
       
    for i in range(numToDel):
        
        rowIndex = int(input("Row number you wish to delete: "))
        csvDF = csvDF.drop(csvDF.iloc[rowIndex].name, inplace = True)
    
    return csvDF