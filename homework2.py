from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
import os
import matplotlib.pyplot as plt


###Merge the 12 months amount of data in one csv
all_months_data = pd.DataFrame()
files = [file for file in os.listdir('/content/drive/MyDrive/DataScience/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data')]
for file in files:
  df = pd.read_csv('/content/drive/MyDrive/DataScience/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/'+file)
  all_months_data = pd.concat([all_months_data,df])

all_months_data.to_csv("all_data.csv", index = False)

###Read in updated data frame
all_data = pd.read_csv('all_data.csv')
all_data.head()

###Augement data with aditional columns

#Task 2 : add Month column
#Drop raws of NaN

nan_df = all_data[all_data.isna().any(axis=1)]
nan_df.head()

all_data = all_data.dropna(how='all')

all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered']) #Make int
all_data['Price Each'] = pd.to_numeric(all_data['Price Each']) #Make float

all_data['Month'] = all_data['Order Date'].str[0:2].astype('int32')

#Add a sales column
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head()

###Question1 : what was the best month in sales? show it in bars
results = all_data.groupby('Month').sum()
months = range(1,13)

plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD')
plt.xlabel('Month Number')
plt.show()
