#Modules 
import matplotlib.pyplot as plt, pandas

#Pandas Function to read the data set
gas_prices = pandas.read_csv("gas_prices.csv")

#Setting graph size
plt.figure(figsize=(8,5))

#Title. Typography done through fontdict in form of dictionary
plt.title("Gas Price of Anglophone Countries 1991-2008", fontdict = {'family': 'serif',
        "weight": "bold", "size": 16,})

#Plotting X and Y coordinates, data for graph. Takes two values (x,y) need to do each country individually
#Order: Y coordinate, X coordinate, color.-, label
plt.plot(gas_prices.Year, gas_prices.UK, "r.-", label = "United Kingdom")
plt.plot(gas_prices.Year, gas_prices.Australia, "y.-", label = "Australia")
plt.plot(gas_prices.Year, gas_prices.Canada, "b.-", label = "Canada")
plt.plot(gas_prices.Year, gas_prices.USA, "g.-", label = "United States")

#Function to display x labels (Country names)
plt.legend()

#Text on x and y
plt.xlabel("Year")
plt.ylabel("Price USD")

#Displaying years to step size of 2
plt.xticks(gas_prices.Year[::2])

#Save an Image of Linegraph when the script is run
plt.savefig('Gas-Prices-Linegraph.png', dpi = 300)

#Function to display graphs
plt.show()