# allow user to manipulate excel or csv file
# 9/26/2023
# CSC221 M2Pro– File Manipulation
# Susanna Quayle
import shutil
import pandas as pd
import runCSV as csvF
import runExcel as xl


# put excel and csv file into data frame to display to user
csvDF = pd.read_csv('M2Pro_CSV.csv')
excelDF = pd.read_excel('M2Pro_Excel.xlsx')

colNames = list(excelDF.columns)
rowNames = list(excelDF.index)

def getFileType():
    # this is the func where user will choose file type
    print("Welcome to File Manipulation")
    print("1. Excel file")
    print("2. CSV file")
    print("3. Exit File Manipulator")
    fileType = int(input("Which type of file would you like to use? "))
    return fileType;


fileType = 0

while fileType != 3:
    
    fileType = getFileType()   
    
    if fileType == 1:
        print("This is the Excel file.")
        shutil.copy("M2Pro_Excel.xlsx", "EmptyExcel.xlsx")
        print(excelDF)
        userDoes = xl.userAction()       
        if userDoes == 1:
            editedExcel = xl.delCols(excelDF)
            print(editedExcel)  
        elif userDoes == 2:
            editedExcel = xl.delRows(excelDF)
            print(editedExcel)
        elif userDoes == 3:
            editedExcel = xl.delBoth(excelDF)
            print(editedExcel)
        else:
            print("Invalid selection, try again.")
    elif fileType == 2:
        print("This is the CSV file.")
        shutil.copy("M2Pro_CSV.csv", "EmptyCSV.csv")
        print(csvDF)
        userDoes = csvF.userAction()
        if userDoes == 1:
            editedCSV = csvF.delCols(csvDF)
            print(editedCSV)
        elif userDoes == 2:
            editedCSV = csvF.delRows(csvDF)
            print(editedCSV)
        elif userDoes == 3:
            editedCSV = csvF.delBoth(csvDF)
            print(editedCSV)
        else:
            print("Invalid selection, try again.")
    elif fileType == 3:
        print("Farewell.")
    else: 
        print("Invalid selection, try again. \n")