# Import the pandas library as pd for data manipulation
import pandas as pd

# Create a 1-dimensional Series named 'mobile' containing mobile phone brands
mobile = pd.Series(['Samsung', 'Iphone', 'Nokia'])
print(mobile)

# Create another 1-dimensional Series named 'bag' containing items related to bags
bag = pd.Series(['pen', 'paper', 'notebook'])
print(bag)

# Combine 'mobile' and 'bag' into a 2-dimensional DataFrame named 'dataframe'
dataframe = pd.DataFrame({"electronic": mobile, "item": bag})
print(dataframe)

# Read a CSV file named "Mobile phone price.csv" into a DataFrame named 'phone_csv'
phone_csv = pd.read_csv("Mobile phone price.csv")
print(phone_csv)

# Save the modified DataFrame 'phone_csv' to a new CSV file named 'modified_phones_csv'
phone_csv.to_csv('modified_phones_csv', index=False)
