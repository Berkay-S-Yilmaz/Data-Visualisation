#Modules 
from optparse import TitledHelpFormatter
import matplotlib.pyplot as plt, pandas

#Pandas read_csv function to read dataset
data = pandas.read_csv("fifa_data.csv")

#Setting graph size
plt.figure(figsize=(6,7))

#Title and label
plt.title("Football Team Player Ratings Comparison (old stats)", fontdict = {'family': 'serif',
        "weight": "bold"})
plt.ylabel("Player Ratings")

#The values in the pie chart
barcelona = data.loc[data.Club == "FC Barcelona"]["Overall"]
madrid = data.loc[data.Club == "Real Madrid"]["Overall"]
psg = data.loc[data.Club == "Paris Saint-Germain"]["Overall"]

#Labels for each box plot representing the team
labels = ["FC Barcelona", "Real Madrid", "Paris Saint-Germain"]

#Box plot function
plt.boxplot([barcelona, madrid, psg], labels=labels)

#Show function to display chart
plt.show()
