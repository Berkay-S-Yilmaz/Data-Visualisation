#%%
#Modules 
from optparse import TitledHelpFormatter
import matplotlib.pyplot as plt, pandas

#Pandas read_csv function to read dataset
data = pandas.read_csv("SF_Data_Jobs.csv")

#Setting graph size
plt.figure(figsize=(7,5))

#The values in the pie chart
ds = data.loc[data["Job_title"] == "Data Scientist"].count()[0]
da = data.loc[data["Job_title"] == "Data Analyst"].count()[0]
de = data.loc[data["Job_title"] == "Data Engineer"].count()[0]

#Title
plt.title("Data Science Job Posting On Glassdoor | San Fransisco | 2020", fontdict = {'family': 'serif',
        "weight": "bold"})

#Labels
labels = ["Data Scientists", "Data Analysts", "Data Engineers"]

#Pie Function
plt.pie([ds, da, de], labels = labels, autopct="%.2f")

#Show function to display figure
plt.show()