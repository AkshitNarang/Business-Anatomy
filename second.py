from flask import Blueprint, render_template,send_file, request, session
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

second = Blueprint("second", __name__, static_folder="static", template_folder="templates")

sheet_id = 'AIzaSyCIwMY2AA2BnbiGob_i8XJfEBr8--e_NK0'

sales = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit?usp=sharing")

filter1 = sales["City"]=="MUMBAI"
filter2 = sales["City"]=="DELHI"
filter3 = sales["City"]=="BANGALORE"
  
Mum = sales.where(filter1)
Del = sales.where(filter2)
Bang = sales.where(filter3)

@second.route("/mumbai")
def mumbai():
    return render_template('mumbai.html', USER_NAME = session['name'],M1 = 'static/graph_Img/Mumbai_Graph/Month.png', M2 = 'static/graph_Img/Mumbai_Graph/Product.png', 
    M3 = 'static/graph_Img/Mumbai_Graph/Total_Time.png',MonthM = mms, ProductLineM = mmp, ByHourM = sbhm)


##################################### MUMBAI 1 #################################


#  sales.groupby(['Month']).sum()
Total_Sales = Mum.groupby('Month').Total.sum()

months = range(1,4)
# print(months)

plt.figure(figsize=(10,7))
color = ['#e01616', '#b4ed2d', '#9e48db']

plt.bar(months, Total_Sales, color = color)

plt.title('Sales By Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })

labels = ['Jaunuary', 'February', 'March']

plt.xticks(months, size = 14, labels = labels)
plt.yticks(size=14)

plt.ylabel('Sales of each Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
plt.xlabel('Months', fontdict= {'fontname': 'Georgia','fontsize': 20 })

plt.savefig('static/graph_Img/Mumbai_Graph/Month.png')


##################################### MUMBAI 2 #################################


Total_Sales = Mum.groupby('Product line').Total.sum()

Product = sales.groupby('Product line')
keys = [pair for pair, df in Product]

plt.figure(figsize=(15,8))

plt.title('Sales Of Product', fontdict= {'fontname': 'Georgia','fontsize': 25 })
colors = ['#4755a6', '#6da32f', '#ad283e', '#d6d01e', '#913d5b', '#5b7fe3']

plt.bar(keys, Total_Sales, color = colors)

plt.xticks(keys, size=12)
plt.yticks(size = 14)

plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 25 })
plt.xlabel('Product Line', fontdict= {'fontname': 'Georgia','fontsize': 25 })

plt.savefig('static/graph_Img/Mumbai_Graph/Product.png')



##################################### MUMBAI 3 #################################



Mum['Hour'] = pd.to_datetime(Mum['TIME']).dt.hour
Mum['Minute'] = pd.to_datetime(Mum['TIME']).dt.minute
Mum['Count'] = 1

keys = [pair for pair, df in Mum.groupby(['Hour'])]

plt.figure(figsize=(9,6))

plt.title('Sales By Hour', fontdict= {'fontname': 'Georgia','fontsize': 20 })

plt.plot(keys, Mum.groupby(['Hour']).count()['Count'], color='#32b865')

plt.xticks(keys,size = 13)
plt.yticks(size = 13)

plt.ylabel('Sales Count', fontdict= {'fontname': 'Georgia','fontsize': 20 })
plt.xlabel('Time in Hours', fontdict= {'fontname': 'Georgia','fontsize': 20 })

plt.grid()

plt.savefig('static/graph_Img/Mumbai_Graph/Total_Time.png')



#monthlysales--------------------------------------------------
mmp=Mum.groupby('Month')['Total'].sum()
mms=list(mmp.keys())[0]

# print(f'best month for sales in mumbai:{mms}')


#productline----------------------------------------------------
ea_m=Mum[Mum['Product line']=='Electronics accessories']['Quantity'].sum()
fa_m=Mum[Mum['Product line']=='Fashion accessories']['Quantity'].sum()
fb_m=Mum[Mum['Product line']=='Food and beverages']['Quantity'].sum()
hb_m=Mum[Mum['Product line']=='Health and beauty']['Quantity'].sum()
hl_m=Mum[Mum['Product line']=='Home and lifestyle']['Quantity'].sum()
sp_m=Mum[Mum['Product line']=='Sports and travel']['Quantity'].sum()
mumbaipl={'electronics accessories':ea_m,'Fashion accessories':fa_m,'Food and Beverages':fb_m,'Health and Beauty':hb_m,'Home and lifestyle':hl_m,'Sports and Travel':sp_m}
mmp=max(mumbaipl,key=mumbaipl.get)
# print(f'the best product line is:{mmp}')


#salesbyhour-----------------------------------------------------
tenm=Mum[Mum['Hour']==10]['Total'].sum()
elvm=Mum[Mum['Hour']==11]['Total'].sum()
twlm=Mum[Mum['Hour']==12]['Total'].sum()
thrm=Mum[Mum['Hour']==13]['Total'].sum()
frtm=Mum[Mum['Hour']==14]['Total'].sum()
fifm=Mum[Mum['Hour']==15]['Total'].sum()
sixm=Mum[Mum['Hour']==16]['Total'].sum()
svnm=Mum[Mum['Hour']==17]['Total'].sum()
eigm=Mum[Mum['Hour']==18]['Total'].sum()
ninm=Mum[Mum['Hour']==19]['Total'].sum()
twnm=Mum[Mum['Hour']==20]['Total'].sum()
salesbyhourmumbai={'10am':tenm,'11am':elvm,'12pm':twlm,'1pm':thrm,'2pm':frtm,'3pm':fifm,'4pm':sixm,'5pm':svnm,'6pm':eigm,'7pm':ninm,'8pm':twnm}
sbhm=max(salesbyhourmumbai,key=salesbyhourmumbai.get)

# print(f'best time for sales:{sbhm}')


##################################### DELHI #################################

@second.route("/delhi")
def delhi():
    return render_template('delhi.html', USER_NAME = session['name'], D1 = 'static/graph_Img/delhi_Graph/Month.png', D2 = 'static/graph_Img/Delhi_Graph/Product.png', 
    D3 = 'static/graph_Img/Delhi_Graph/Total_Time.png', MonthD = dms, ProductLineD = dmp_d, ByHourD = sbhd)       


    #  sales.groupby(['Month']).sum()
Total_Sales = Del.groupby('Month').Total.sum()

months = range(1,4)
    # print(months)

plt.figure(figsize=(10,7))
color = ['#e01616', '#b4ed2d', '#9e48db']

plt.bar(months, Total_Sales, color = color)

plt.title('Sales By Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })

labels = ['Jaunuary', 'February', 'March']

plt.xticks(months, size = 14, labels = labels)
plt.yticks(size=14)

plt.ylabel('Sales of each Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
plt.xlabel('Months', fontdict= {'fontname': 'Georgia','fontsize': 20 })

plt.savefig('static/graph_Img/Delhi_Graph/Month.png')







Total_Sales = Del.groupby('Product line').Total.sum()
Product = Del.groupby('Product line')
keys = [pair for pair, df in Product]

plt.figure(figsize=(15,8))

plt.title('Sales Of Product', fontdict= {'fontname': 'Georgia','fontsize': 25 })
colors = ['#4755a6', '#6da32f', '#ad283e', '#d6d01e', '#913d5b', '#5b7fe3']
   
plt.bar(keys, Total_Sales, color = colors)
   
plt.xticks(keys, size=12)
plt.yticks(size = 14)
   
plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 25 })
plt.xlabel('Product Line', fontdict= {'fontname': 'Georgia','fontsize': 25 })
   
plt.savefig('static/graph_Img/Delhi_Graph/Product.png')
   





Del['Hour'] = pd.to_datetime(Del['TIME']).dt.hour
Del['Minute'] = pd.to_datetime(Del['TIME']).dt.minute
Del['Count'] = 1

keys = [pair for pair, df in Del.groupby(['Hour'])]
Total_Sales_Del = Del.groupby(['Hour']).count()['Count']

plt.figure(figsize=(9,6))

plt.title('Sales By Hour', fontdict= {'fontname': 'Georgia','fontsize': 20 })

plt.plot(keys, Total_Sales_Del , color='#32b865')

plt.xticks(keys,size = 13)
plt.yticks(size = 13)

plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 20 })
plt.xlabel('Time in Hours', fontdict= {'fontname': 'Georgia','fontsize': 20 })

plt.grid()

plt.savefig('static/graph_Img/Delhi_Graph/Total_Time.png')


#monthlysales--------------------------------------------------
dmp=Del.groupby('Month').Total.sum()
dms=list(dmp.keys())[0]

# print(f'best month for sales in delhi:{dms}')


#productline----------------------------------------------------
ea_d=Del[Del['Product line']=='Electronics accessories']['Quantity'].sum()
fa_d=Del[Del['Product line']=='Fashion ccessories']['Quantity'].sum()
fb_d=Del[Del['Product line']=='Food and beverages']['Quantity'].sum()
hb_d=Del[Del['Product line']=='Health and beauty']['Quantity'].sum()
hl_d=Del[Del['Product line']=='Home and lifestyle']['Quantity'].sum()
sp_d=Del[Del['Product line']=='Sports and travel']['Quantity'].sum()
delhipl={'electronics accessories':ea_d,'Fashion accessories':fa_d,'Food and beverages':fb_d,'Health and Beauty':hb_d,'Home and lifestyle':hl_d,'Sports and Travel':sp_d}
dmp_d=max(delhipl,key=delhipl.get)
# print(f"product line with the most sales is:{dmp_d}")


#salesbyhour-----------------------------------------------------
tend=Del[Del['Hour']==10]['Total'].sum()
elvd=Del[Del['Hour']==11]['Total'].sum()
twld=Del[Del['Hour']==12]['Total'].sum()
thrd=Del[Del['Hour']==13]['Total'].sum()
frtd=Del[Del['Hour']==14]['Total'].sum()
fifd=Del[Del['Hour']==15]['Total'].sum()
sixd=Del[Del['Hour']==16]['Total'].sum()
svnd=Del[Del['Hour']==17]['Total'].sum()
eigd=Del[Del['Hour']==18]['Total'].sum()
nind=Del[Del['Hour']==19]['Total'].sum()
twnd=Del[Del['Hour']==20]['Total'].sum()
salesbyhourdelhi={'10am':tend,'11am':elvd,'12pm':twld,'1pm':thrd,'2pm':frtd,'3pm':fifd,'4pm':sixd,'5pm':svnd,'6pm':eigd,'7pm':nind,'8pm':twnd}
sbhd=max(salesbyhourdelhi,key=salesbyhourdelhi.get)
# print(f'best time for sales:{sbhd}')


########################################## BANGALORE #####################################


@second.route("/bangalore")
def bangalore():
    return render_template('bangalore.html', USER_NAME = session['name'], B1 = 'static/graph_Img/Bangalore_Graph/Month.png', B2 = 'static/graph_Img/Bangalore_Graph/Product.png', B3 = 'static/graph_Img/Bangalore_Graph/Total_Time.png', MonthB = bms, ProductLineB = dmp_b, ByHourB = bsh_b) 


#  sales.groupby(['Month']).sum()
Total_Sales = Bang.groupby('Month').Total.sum()

months = range(1,4)
# print(months)

plt.figure(figsize=(10,7))
color = ['#e01616', '#b4ed2d', '#9e48db']

plt.bar(months, Total_Sales, color = color)
    
plt.title('Sales By Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })

labels = ['Jaunuary', 'February', 'March']

plt.xticks(months, size = 14, labels = labels)
plt.yticks(size=14)

plt.ylabel('Sales of each Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
plt.xlabel('Months', fontdict= {'fontname': 'Georgia','fontsize': 20 })

plt.savefig('static/graph_Img/Bangalore_Graph/Month.png')




Total_Sales = Bang.groupby('Product line').Total.sum()

Product = Bang.groupby('Product line')
keys = [pair for pair, df in Product]

plt.figure(figsize=(14,8))

plt.title('Sales Of Product', fontdict= {'fontname': 'Georgia','fontsize': 25 })
colors = ['#4755a6', '#6da32f', '#ad283e', '#d6d01e', '#913d5b', '#5b7fe3']

plt.bar(keys, Total_Sales, color = colors)

plt.xticks(keys, size=12)
plt.yticks(size = 14)

plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 25 })
plt.xlabel('Product Line', fontdict= {'fontname': 'Georgia','fontsize': 25 })

plt.savefig('static/graph_Img/Bangalore_Graph/Product.png')




Bang['Hour'] = pd.to_datetime(Bang['TIME']).dt.hour
Bang['Minute'] = pd.to_datetime(Bang['TIME']).dt.minute
Bang['Count'] = 1

keys = [pair for pair, df in Bang.groupby(['Hour'])]
Total_Sales = Bang.groupby(['Hour']).count()['Count']

plt.figure(figsize=(9,6))

plt.title('Sales By Hour', fontdict= {'fontname': 'Georgia','fontsize': 20 })

plt.plot(keys, Total_Sales, color='#32b865')

plt.xticks(keys,size = 13)
plt.yticks(size = 13)

plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 20 })
plt.xlabel('Time in Hours', fontdict= {'fontname': 'Georgia','fontsize': 20 })

plt.grid()

plt.savefig('static/graph_Img/Bangalore_Graph/Total_Time.png')



#monthlysales--------------------------------------------------
bmp=Bang.groupby('Month')['Total'].sum()
bms=list(bmp.keys())[0]
# print(f'best month for sales in bangalore:{bms}')

#productline----------------------------------------------------
ea_b=Bang[Bang['Product line']=='Electronics accessories']['Quantity'].sum()
fa_b=Bang[Bang['Product line']=='Fashion ccessories']['Quantity'].sum()
fb_b=Bang[Bang['Product line']=='Food and beverages']['Quantity'].sum()
hb_b=Bang[Bang['Product line']=='Health and beauty']['Quantity'].sum()
hl_b=Bang[Bang['Product line']=='Home and lifestyle']['Quantity'].sum()
sp_b=Bang[Bang['Product line']=='Sports and travel']['Quantity'].sum()
bangalorepl={'electronics accessories':ea_b,'Fashion accessories':fa_b,'Food and Beverages':fb_b,'Health and Beauty':hb_b,'Home and Lifestyle':hl_b,'Sports and Travel':sp_b}
dmp_b=max(bangalorepl,key=bangalorepl.get)
# print(f'best product line in bangalore is:{dmp_b}')

#salesbyhour-----------------------------------------------------
Bang['Hour']=pd.to_datetime(Bang['TIME']).dt.hour
Bang['Minute']=pd.to_datetime(Bang['TIME']).dt.minute
Bang['Count']=1
bsh=Bang.groupby('Hour')['Total'].sum()
bsh_b=list(bsh.keys())[0]
# print(f'best time for sales:{bsh_b}am')
