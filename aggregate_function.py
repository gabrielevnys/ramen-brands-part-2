import pandas as pd

print("Basic Exploratory Analysis on Ramen Brands Part 2\n\n")


#read the CSV file
df = pd.read_csv("ramen-ratings.csv")

#data types
print("Below are the data types of the dataframe:", df.dtypes, end="\n\n", sep="\n")

#change the "Stars" data type into float
df["Stars"] = pd.to_numeric(df["Stars"], errors="coerce")
print("The new data types: ", df.dtypes, end="\n\n", sep="\n")

#find the average rating of each ramen brand using aggregate function
rating_avg = df["Stars"].groupby(df["Brand"]).mean()
print("Rating average of each ramen brand using the aggregate function:", rating_avg, end="\n\n", sep="\n")

#sort values
print("Sort the ramen brand based on average rating:")
print(rating_avg.sort_values(ascending=False), end="\n\n")

print(df.sort_values(by="Stars", ascending=False))
