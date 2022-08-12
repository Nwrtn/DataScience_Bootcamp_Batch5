# import data
import pandas as pd
df = pd.read_csv("sample-store.csv")


# preview top 5 rows
df.head()


# shape of dataframe
df.shape


# see data frame information using .info()
df.info()


# example of pd.to_datetime() function
pd.to_datetime(df['Order Date'].head(), format='%m/%d/%Y')



# TODO - convert order date and ship date to datetime in the original dataframe

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')
df



# TODO - count nan in postal code column

df['Postal Code'].isna().sum()



# TODO - filter rows with missing values

df['Postal Code'].isna()

df = df.dropna()
df.reset_index()



# TODO - Explore this dataset on your owns, ask your own questions

# top 10 customers in New York

df_NY = df[df['State'] == 'New York']

df_NY


df_NY.groupby(['City', 'Customer ID', 'Customer Name'])['Sales']\
    .agg(['sum','min', 'mean', 'max'])\
    .sort_values('sum', ascending=False)\
    .reset_index()\
    .head(10)


# which city in New York has the highest total sales


df_NY.groupby('City')['Sales']\
    .agg(['sum','min', 'mean', 'max'])\
    .sort_values('sum', ascending=False)\
    .reset_index()



## Data Analysis Part
## Answer 10 below questions to get credit from this course. Write pandas code to find answers.


# TODO 01 - how many columns, rows in this dataset
df.shape



# TODO 02 - is there any missing values?, if there is, which colunm? how many nan values?

df.info()

df.isna().sum()



# TODO 03 - your friend ask for `California` data, filter it and export csv for him

# 03.1 select data from California

df[df['State'] == 'California']

df_CA = df[df['State'] == 'California']

df_CA

# 03.2 export csv file

df_CA.to_csv('df_california.csv', index=False)




# TODO 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
# 04.1 select data from California and Texas

df_CA_TX = df.query('State == "California" | State == "Texas"')

df_CA_TX

# 04.2 select data from 2017

df_2017_CA_TX = df_CA_TX[df_CA_TX['Order Date'].dt.year == 2017]

df_2017_CA_TX

# 04.3 export csv file of df_2017_CA_TX

df_2017_CA_TX.to_csv('df_2017_CA_TX.csv', index=False)



# TODO 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017

# 05.1 select data from 2017

df2017 = df[df['Order Date'].dt.year == 2017]

df2017

# 05.2 summarise Sales column

df2017['Sales'].describe()

# 05.3 Function to use for aggregating the data

df2017['Sales'].agg(['sum', 'mean', 'std'])




# TODO 06 - which Segment has the highest profit in 2018

# 06.1 select data from 2018

df2018 = df[df['Order Date'].dt.year == 2018]

df2018

# 06.2 Group by Segment and aggregate Profit column

df2018.groupby('Segment')['Profit'].agg(['sum', 'max'])




# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019

# 07.1 Select data between 15 April 2019 - 31 December 2019

df2019_APR15_to_DEC31 = df[(df['Order Date'] >= '2019-04-15') & (df['Order Date'] <= '2019-12-31')]

df2019_APR15_to_DEC31

# 07.2 group by State, sum, and sort

df2019_APR15_to_DEC31.groupby('State')['Sales'].sum().sort_values().head(10)




# TODO 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 

# 08.1 Select data from 2019

df2019 = df[df['Order Date'].dt.year == 2019]

df2019

# 08.2 select data from Region West and Central

df2019_Cen_W = df2019.query('Region == "Central" | Region == "West"')

df2019_Cen_W

# 08.3 sum Sales column of df2019_Cen_W

sale2019CenW = df2019_Cen_W['Sales'].sum()

sale2019CenW

# 08.4 sum Sales column of df2019 (Total sales)

sale2019Total = df2019['Sales'].sum()

sale2019Total

# 08.5 proportion of total sales

proportion = (sale2019CenW / sale2019Total)*100

print(f"{proportion.round(2)} % of total sales")




# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020

# 09.1 select data from 2019-2020

df2019_2020 = df[(df['Order Date'].dt.year == 2019) | (df['Order Date'].dt.year == 2020)]

df2019_2020

# 09.2 top 10 popular products in terms of number of orders

top10_product_order = df2019_2020['Product Name'].value_counts().head(10)

top10_product_order

# 09.2.1 top 10 popular products in terms of number of Quantity

top10_product_order_qty = df2019_2020.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False).head(10)

top10_product_order_qty

# 09.3 top 10 products in terms of total sales

top10_product_sales = df2019_2020.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

top10_product_sales




# TODO 10 - plot at least 2 plots, any plot you think interesting :)

df2020 = df[df['Order Date'].dt.year == 2020]

df2020


# 10.1 top sub-category in terms of number of orders in 2020

df2020['Sub-Category'].value_counts().plot(kind='bar', color = '#91B1E1');


# 10.2 top sub-category in terms of total sales in 2020

df2020.groupby(['Category', 'Sub-Category'])['Sales'].sum()\
    .sort_values(ascending=False).head(10)\
    .plot(kind = 'bar',\
          color=['#03045e', '#023e8a', '#0077b6', '#0096c7', '#00b4d8', '#48cae4', '#90e0ef', '#ade8f4', '#caf0f8', '#E4EBF1'])




# TODO Bonus - use np.where() to create new column in dataframe to help you answer your own questions

import numpy as np

df2020['with_discount'] = np.where(df2020['Discount']>0, True, False)

df2020

df2020['with_discount'].value_counts()
