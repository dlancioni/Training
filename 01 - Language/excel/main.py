# coding=UTF-8
import os
os.system("cls || clear")

import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

filepath = "c:\\temp\\python_demo.xls"

def create():
    workbook = openpyxl.Workbook()
    sheet1 = workbook.create_sheet("Saldo")
    sheet2 = workbook.create_sheet("Extrato")
    workbook.save(filepath)
    
def open():   
    workbook = load_workbook(filename = filepath)
    sheet1 = workbook["Saldo"]
    sheet1.cell(1, 1).value = "David"
    workbook.save(filepath)
    
#create()    
open()    