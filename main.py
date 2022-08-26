import pandas as pd
print("Hello ,World ! ")
print("Hello this is my name:" + input("Name here"))
print("Hello this is my Second name:" +  input("Second Name here"))
x = int(input("x value :"))
y = x *2
z = y * 20
print(z)

  
# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc'],
        'Contacts': [90303888,90303887,2387848,0]
       }
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Declare a list that is to be converted into a column
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
weight = [67.3, 67.9,89.5,80]
  
# Using 'Address' as the column name
# and equating it to the list
df['Address'] = address 
df['Weight'] = weight  
# Observe the result
print(df)
