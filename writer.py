#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:30:26 2020

@author: Pedro_Martínez
"""

from openpyxl import load_workbook

filepath=r'/Users/macbookpro/Desktop/Python_excercises/Multiflap/1000/1000_summary_normal_cases_analysis.xlsx'

def write(filepath=filepath,contenido, hoja, columna, fila, inc_fila, incr_col):

    wb = load_workbook(filepath)
    sheets=wb.sheetnames
    sheet1=wb[sheets[2]]
    
    for val in contenido:
        sheet1.cell(row=fila,column=columna).value= val
        columna+=incr_col
        fila+=inc_fila