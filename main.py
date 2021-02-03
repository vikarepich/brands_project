###Assortment analysis of the two denim brands: Levi's and G-Star RAW

##Data import
#Load the relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##Read data from csv files into dataframes using pandas
#G-Star RAW assorment
gstar_df = pd.read_csv('gstar_price.csv', ';')
#Levi's assorment
levis_df = pd.read_csv('levis_price.csv', ';')

##Data explore
#Get the column structure of the datasets.
#G-Star RAW dataset
gstar_df.info()
print(gstar_df.shape)
#Levi's dataset
levis_df.info()
print(levis_df.shape)
#Sampling G-Star RAW dataset records
gstar_df.head(4)
#Sampling Levi's dataset records
levis_df.head(4)

##Data prepare
#To avoid issues related with casing and spaces in column names, we replace the spaces with '_' in both datasets.
#And further convert all names to lowercase.
levis_df.columns = levis_df.columns.str.replace('\s+', '_').str.lower().str.strip()
gstar_df.columns = gstar_df.columns.str.replace('\s+', '_').str.lower().str.strip()

#Check gender and concept statistics
concept_statistics_levis = levis_df.concept.value_counts()
gender_statistics_levis = levis_df.gender.value_counts()
concept_statistics_gstar = gstar_df.concept.value_counts()
gender_statistics_gstar = gstar_df.gender.value_counts()

##Check for duplicates in the Levi's & G-Star RAW dataset
if (levis_df.duplicated().any()):
    duplicatesAmount = sum(levis_df.duplicated())
    print(f"The amount of duplicates are {duplicatesAmount}")
else:
    print("There are no duplicates")
levis_df = levis_df[~levis_df.duplicated()]

if (gstar_df.duplicated().any()):
    duplicatesAmount = sum(gstar_df.duplicated())
    print(f"The amount of duplicates are {duplicatesAmount}")
else:
    print("There are no duplicates")
gstar_df = gstar_df[~gstar_df.duplicated()]
print(levis_df.shape)

##Data merge
#Two datasets have same structure, we can merge them to have a one dataset for easier analysis
merge_df = levis_df.append(gstar_df)
merge_df.to_csv('merged_data.csv', index = False)
merge_df.shape
print(levis_df.describe())
print(gstar_df.describe())
print(merge_df.describe())

##Assorment analysis
#It's logical to start assortment analysis from general to specific
#Which gender id ley for each brand?
#Levi's
levis_df.gender.value_counts()
levis_women_df = levis_df[levis_df.gender.isin(['Women'])]
levis_women_models_amount = levis_women_df.gender.count()
levis_df.gender.value_counts()
levis_men_df = levis_df[levis_df.gender.isin(['Men'])]
levis_men_models_amount = levis_men_df.gender.count()
if(levis_women_models_amount > levis_men_models_amount):
    print(f"Levis focuses on women {levis_women_models_amount} vs {levis_men_models_amount} ")
else:
    print(f"Levis focuses on men {levis_men_models_amount} vs {levis_women_models_amount} ")
#G-Star RAW
gstar_df.gender.value_counts()
gstar_women_df = gstar_df[gstar_df.gender.isin(['Women'])]
gstar_women_models_amount = gstar_women_df.gender.count()
gstar_df.gender.value_counts()
gstar_men_df = gstar_df[gstar_df.gender.isin(['Men'])]
gstar_men_models_amount = gstar_men_df.gender.count()
if(gstar_women_models_amount > gstar_men_models_amount):
    print(f"Gstar focuses on women {gstar_women_models_amount} vs {gstar_men_models_amount} ")
else:
    print(f"Gstar focuses on men {gstar_men_models_amount} vs {gstar_women_models_amount} ")

#According to the fact, that this is apparel brands, let's check what assortment these brands offer
gender_comparison_result = merge_df.groupby(["brand", "gender"])["article"].count()
print(f'Assortment analysis split gender: \n{gender_comparison_result} ')
segment_comparison_result = merge_df.groupby(["brand", "segment_hq"])["article"].count()
print(f'Assortment analysis split segment: \n{segment_comparison_result} ')
type_comparison_result = merge_df.groupby(["brand", "gender", "type"])["article"].count()
print(f'Assortment analysis split type: \n{type_comparison_result} ')

#According to the fact, that this is denim brands, let's check what denim fits available there
gender_comparison_result = merge_df.groupby(["brand", "gender"])["article"].count()
print(f'Assortment analysis split gender: \n{gender_comparison_result} ')
segment_comparison_result = merge_df.groupby(["brand", "segment_hq"])["article"].count()
print(f'Assortment analysis split segment: \n{segment_comparison_result} ')
fit_comparison_result = merge_df.groupby(["brand", "gender", "fit"])["article"].count()
print(f'Assortment analysis split fit: \n{fit_comparison_result} ')

#Price analysis (Prices in Rubles (Russian currecy))
print(levis_df.dtypes)
levis_df['rrp'] = levis_df['rrp'].astype(int)
print(f"Levis has prices between: {levis_df['rrp'].min()} and {levis_df['rrp'].max()}")
print(f"G-Star RAW has prices between: {gstar_df['rrp'].min()} and {gstar_df['rrp'].max()}")
levis_average_price = levis_df['rrp'].median()
gstar_average_price = gstar_df['rrp'].median()
if (levis_average_price > gstar_average_price):
    print(f"Levis's price policy is lower. Median price is {levis_average_price} RUB")
else:
    print(f"Gstar's price policy is lower. Median price is {gstar_average_price} RUB")

#Let's have point check to assure that data is correct in merge and source csv files
merge_df.segment_hq.value_counts()
levis_df.segment_hq.value_counts()
gstar_df.segment_hq.value_counts()
levis_j_df = levis_df[levis_df.segment_hq.isin(['APP MEN'])]
levis_j_df = levis_j_df[levis_j_df['type'].str.contains('Jeans')]
levis_jeans_count = levis_j_df['type'].str.contains('Jeans').value_counts()
print(f'Count of Jeans Products: {levis_jeans_count} ')
print(levis_j_df['type'].str.contains('Jeans').value_counts())
gstar_s_df = merge_df[merge_df.segment_hq.isin(['APP MEN'])]
gstar_s_df = gstar_s_df[gstar_s_df['name'].str.contains('Skinny')]
print('Count of Skinny Products: \n ')
gstar_a_df = merge_df[merge_df.segment_hq.isin(['APP MEN'])]
gstar_a_df = gstar_a_df[gstar_a_df['name'].str.contains('Arc')]
print('Count of Arc Products: \n ')

##Visualisation
#To understand data better its quite useful to visualise analysis
#Let's see what is the assortment is presented in Levi's
sns.set(font_scale=0.9)
plt.figure(figsize=(10, 6))
levis_df.segment_hq.value_counts().plot(kind = 'bar', rot = 0, color = ['red', 'green', 'blue', 'orange', 'yellow', 'black'])
plt.xlabel('Segment')
plt.ylabel('Quantity')
plt.title('Distribution of Segments for Levis')
plt.show()

#Let's see what is the assortment is presented in G-Star RAW
sns.set(font_scale=0.9)
plt.figure(figsize=(10, 6))
gstar_df.segment_hq.value_counts().plot(kind = 'bar', rot = 0, color = ['red', 'green', 'blue', 'orange', 'yellow', 'black'])
plt.xlabel('Segment')
plt.ylabel('Quantity')
plt.title('Distribution of Segments for G-Star RAW')
plt.show()
print('Tabular Segment Distibution: \n')

#Now let's observe price differentiation in two brands (Prices in Rubles (Russian currecy))
sns.distplot(levis_df['rrp'], kde = False, color='blue', label='The Levis prices', hist_kws={"range": [400, 30000]})
sns.distplot(gstar_df['rrp'], kde = False, color='red', label='The G-Star RAW prices', hist_kws={"range": [400, 30000]})
plt.xlabel("Sale Price", labelpad=14)
plt.ylabel("Frequency", labelpad=14)
plt.title("Histogram of Sale Price (in Russian Rubles)", fontsize=14, y=1.01)
plt.legend()
plt.show()

##Thank you for the Python course :)



