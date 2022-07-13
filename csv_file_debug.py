# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:18:55 2021

@author: CZHA43
"""

def open_CSV_file(file_name):
    import pandas as pd
    import csv
    try:
        f=open(file_name,'r',encoding='utf-8')
        data1=pd.read_csv(f,engine='python')
    except Exception:
        print('method1 died')
    try:
        csv_reader = csv.reader(open(file_name,encoding='utf-8'))
        data2=pd.DataFrame(csv.reader)
    except Exception:
        print('method2 died')
    try:
        data3=pd.read_csv(f,engine='gbk',header=none)
    except Exception:
        print('method3 died')
    try:
        csv_reader = csv.reader(open(file_name,encoding='gbk'))
        data4=pd.DataFrame(csv.reader)
    except Exception:
        print('method4 died')
    try:
        data5=pd.read_csv(file_name,header=0,engine='gbk',error_bad_lines=False)
    except Exception:
        print('method5 died')
    try:
        f=open(file_name,'r',encoding='ISO-8859-1')
        data6=pd.read_csv(f,engine='python')
    except Exception:
        print('method6 died')
    try:
        f=open(file_name,'r',encoding='gb18030')
        data7=pd.read_csv(f,engine='python')
    except Exception:
        print('method7 died')
    try:
        f=open(file_name,'r')
        lines = f.readlines()
        for line in lines:
            return line
    except Exception:
        print('method8 died')
        
open_CSV_file(r'C:\Users\czha43\Desktop\sourcing\20211111.xls')
    