#Modules 
import matplotlib.pyplot as plt, pandas

#Pandas read_csv function to read dataset
data = pandas.read_csv("fifa_data.csv")

#Title
plt.title("Fifa Players Overall Skill Chart", fontdict = {'family': 'serif',
        "weight": "bold", "size": 16,})

#The intervals of skills level levels
bins = [40,50,60,70,80,90]

#Matplotlip hist() function to create histogram
plt.hist(data.Overall, bins=bins, color="#031cfc")

# X-axis & Y-axis texts
plt.ylabel("Player Count")
plt.xlabel("Player Skill Level")

#Show function to show graph
plt.show()