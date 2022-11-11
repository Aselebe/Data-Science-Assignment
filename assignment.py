# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 19:03:23 2022

@author: Aselebe Michael Oluwasegun

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


"""reading the data from https://finances.worldbank.org/api/views/k6tm-smim
/rows.csv?accessType=DOWNLOAD
"""


finance = \
pd.read_csv("https://finances.worldbank.org/api/views/k6tm-smim/rows.csv?accessType=DOWNLOAD")

#Printing the pandas to be sure they are fully in the right format

print(finance)

# changing the title of the Total amount of loan to Total disbursement 

finance = finance.rename(columns = {"Total":"Total Disbursement"})



# deleting inrelevant columns in the dataframe

finance = finance.drop(columns = ["Program for Results", 
                                  "Private Sector Window" ])

print(finance)

#First saving to excel sheet

finance.to_csv("finance.csv")

#Renaming Columns 

finance = finance.rename(columns = {"Region":"Sub-Region"}, )

finance = finance.rename(columns = {"Development Policy":"Gap"})

finance = finance.dropna()

#Replacing columns 

finance["New Region"] = finance['Sub-Region'].replace(['AFRICA EAST',
                    'AFRICA WEST',  'EASTERN AND SOUTHERN AFRICA', 
                    'MIDDLE EAST AND NORTH AFRICA' , 
                    'WESTERN AND CENTRAL AFRICA'    ],
                   ['AFRICA', 'AFRICA','AFRICA','AFRICA','AFRICA'])

finance["Year"] = finance['Time Period'].replace(["FY14" ,"FY15", "FY16"	, 
                   "FY17"	, "FY18"	 ,"FY19",
                    "FY20"	 ,"FY21"	,"FY22", "FY23-Q1"	 ],
                     [2014, 2015, 2016, 2017,
                    2018, 2019, 2020, 2021, 2022,2023 ])


# second saving to excel sheet 

finance.to_csv("IDA.csv")

print(finance)


#calculating the average and Median

print("Average:")
print(finance.mean())

print(" \n Median:")
print(finance.median())


#Grouping the Data

total_disbursement = finance.groupby("New Region")["Total Disbursement"].sum()

category = finance.groupby("Year")["Total Disbursement"].sum()
category1 = finance.groupby("Year")["Investment Lending"].sum()
category2 = finance.groupby("Year")["Gap"].sum()

category_class = [category,category1,category2]

print(category_class)


"""
This function is to crear a Line chart and it include the for yearly 
disbursement of loans by IDA and IBRD

"""
#FUNCTION TO CREAT FINANCE Line CHART FOR YEARLY DISBURSEMENT

def linechart(data1, data2,data3):

    plt.figure()
    category.plot( color = "Purple")
    category1.plot( color = "Red")
    category2.plot( color = "Green")
    plt.title("2014-2022 IBRD and  IDA Loan Report", size = 15)
    plt.ylabel("Loan Amount")
    labels = ['Total Disbursement', 'Investment Lending', 'Gap']
    plt.x_limit = (finance["Year"])
    plt.legend()
    plt.tight_layout()

    plt.show()
    
linechart(category, category1,category2)


"""
This function is to creat a Bar chart

"""

def barchart(data):

    plt.figure()
    category.plot.bar( color = "purple")
    plt.title("Yearly Total Disbursement", size = 14)
    plt.show()

barchart(category)



df_finance = finance.groupby("New Region").count()

pie_graph = df_finance["Total Disbursement"]

label = df_finance.index

explode = [0.1,0,0,0,0,0]

autopct='%1.1f%%'

"""
This function is to creat a Pie chart and it include the label , explode and others
"""
def create_pie (data, explode, label, autopct):

    plt.pie (pie_graph, explode = explode, labels = label, autopct=autopct)
    plt.title("Regional Report", size = "18")
    plt.show()

create_pie (pie_graph, explode, label,autopct)

#Resaving final sheet.

finance.to_excel("The final Finance.xlsx")

