from turtle import width
from flask import Blueprint
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

second1 = Blueprint("second1", __name__, static_folder="static", template_folder="templates")

pd.set_option('display.max_columns', None)

sales = pd.read_csv('static/csv/supermarket_sales.csv')

def TotalSales_WRT_Month(filename):
    Total_Sales = sales.groupby('Month').Total.sum()
    months = range(1,4)
        
    plt.figure(figsize=(10,7))
    colors = ['#e01616', '#612f75', '#db3d7a']
        
    plt.bar(months, Total_Sales, color = colors)
        
    plt.title('Sales By Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
        
    labels = ['Jaunuary', 'February', 'March']
    plt.xticks(months, size = 14, labels = labels)
    plt.yticks(size=14)
        
    plt.ylabel('Sales of each Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.xlabel('Months', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    
    export_picture(filename)

def TotalSales_WRT_City(filename):
# Delhi = sales.loc[sales['City'] == 'DELHI'].count()[0]
# Mumbai = sales.loc[sales['City'] == 'MUMBAI'].count()[0]
# Bangalore = sales.loc[sales['City'] == 'BANGALORE'].count()[0]

    Mumbai = sales.loc[sales['City'] == 'MUMBAI'].Total.sum().astype(int)
    Delhi = sales.loc[sales['City'] == 'DELHI'].Total.sum().astype(int)
    Bangalore = sales.loc[sales['City'] == 'BANGALORE'].Total.sum().astype(int)

    labels = ['Mumbai', 'Delhi', 'Bangalore']
    # colors = ['#4755a6', '#6da32f']
    explode = (0.1,0.1,0.1)

    plt.pie([Delhi,Mumbai,Bangalore], labels = labels, explode = explode, autopct = '%.2f %%', radius=1.5,textprops={'fontsize': 15} )

    export_picture(filename)


def TotalSales_WRT_Time(filename):
    sales['Hour'] = pd.to_datetime(sales['TIME']).dt.hour
    sales['Minute'] = pd.to_datetime(sales['TIME']).dt.minute
    sales['Count'] = 1

    keys = [pair for pair, df in sales.groupby(['Hour'])]

    plt.figure(figsize=(9,6))

    plt.title('Sales By Hour', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.plot(keys, sales.groupby(['Hour']).count()['Count'], color='#32b865')

    plt.xticks(keys,size = 13)
    plt.yticks(size = 13)

    plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    plt.xlabel('Time in Hours', fontdict= {'fontname': 'Georgia','fontsize': 20 })

    plt.grid()

    export_picture(filename)

def TotalSales_WRT_Product_Line(filename):
    Total_Sales = sales.groupby('Product line').Total.sum()

    Product = sales.groupby('Product line')
    keys = [pair for pair, df in Product]

    plt.figure(figsize=(10,6))

    plt.title('Sales Of Product', fontdict= {'fontname': 'Georgia','fontsize': 20 })
    colors = ['#4755a6', '#6da32f', '#ad283e', '#d6d01e', '#913d5b', '#5b7fe3']

    plt.bar(keys, Total_Sales, color = colors)

    plt.xticks(keys, size=13)
    plt.yticks(size = 14)

    plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 30 })
    plt.xlabel('Product Line', fontdict= {'fontname': 'Georgia','fontsize': 30 })

    export_picture(filename)

# def TotalSales_WRT_Month(filename):

# def TotalSales_WRT_Month(filename):

# def TotalSales_WRT_Month(filename):

def export_picture(filename):
    plt.legend()
    plt.savefig(filename)
    plt.close

TotalSales_WRT_Month("Month")
TotalSales_WRT_City("City")
TotalSales_WRT_Time("Time")
TotalSales_WRT_Product_Line("Product")


pdf = FPDF()
WIDTH = 210
HEIGHT = 297
pdf.add_page()
pdf.image("Month.png", 5, 20, WIDTH / 2 -5)
pdf.image("City.png", WIDTH / 2 + 5, 20, WIDTH / 2 -5)
pdf.image("Time.png", 5, 90, WIDTH / 2 -5)
pdf.image("Product.png", WIDTH / 2 + 5, 90, WIDTH / 2 -5)

pdf.output("analysis.pdf",'F')

