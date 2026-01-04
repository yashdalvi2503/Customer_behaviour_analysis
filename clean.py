import pandas as pd

df = pd.read_csv(
    "/Users/yashdalvi/serious project/customer_shopping_behavior.csv"
)

#print(df) #show database

#df.info()#info about the rows col

print(df.describe(include="all")) # desc the things

print(df.isnull().sum()) # this shows the null value and some of them 

#remove the null ones 
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum()) # null val gone

# arranged the cloumns name in lower and remove the spaces
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")
df=df.rename(columns={"purchase_amount_(usd)":"purchased_amount"})
print(df.columns) 

#to make the age group like qcut is used it analyses all ages values and make it simple 
lables=["young","adult","mid-aged","senior"]
df["age_group"]=pd.qcut(df["age"],q=4,labels= lables )
print(df[["age","age_group"]].head(10)) 


# there are frequemcy text form tranfer in the numeric form
# lets make a dictonary 
dic={
    "Fortnightly":14,
    "Weekly":7,
    "Annually":365,
    "Quarterly":90,
    "Bi-Weekly":14,
    "Every 3 Months":90
}

df["purchase_frequency_days"]=df["frequency_of_purchases"].map(dic)

print(df[["purchase_frequency_days","frequency_of_purchases"]].head(20))

print((df["discount_applied"]==df["promo_code_used"]).all()) #sqame colm ahet lets drop ome 
df=df.drop("promo_code_used",axis=1)
print(df.columns)
#after cleaning save csv file like this
df.to_csv(
    "/Users/yashdalvi/serious project/customer_shopping_behavior_cleaned.csv",
    index=False
)

df_check = pd.read_csv(
    "/Users/yashdalvi/serious project/customer_shopping_behavior_cleaned.csv"
)
print(df_check.head())



