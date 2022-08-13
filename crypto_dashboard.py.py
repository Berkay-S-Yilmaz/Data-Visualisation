#Yahoo Finance API to get the live cryptocurrency prices
import yfinance
#streamlit to visualize the data and make the web app
import streamlit
#Python Image library to get logos of Cryptocurrencies
from PIL import Image
#Images are located on url. urlopen will open urls, allowing access to the images
from urllib.request import urlopen
#__________________________________________________________________________________#

#Titles, Headings, Subheading etc.
streamlit.title("Cryptocurrency Prices (USD)")
streamlit.header("This web app retreives data on the prices of popular cryptocurrencies using the Yahoo Finance API")


#Creating Ticker Objects
Bitcoin = "BTC-USD"
Ethereum = "ETH-USD"
Cardano = "ADA-USD"
Solana = "SOL-USD"

#Accessing Live/Curent Price Data Via Yahoo Finance 
Bitcoin_Data = yfinance.Ticker(Bitcoin)
Ethereum_Data = yfinance.Ticker(Ethereum)
Cardano_Data = yfinance.Ticker(Cardano)
Solana_Data = yfinance.Ticker(Solana)

#Accessing History Price Data Via Yahoo Finance
Bitcoin_History = Bitcoin_Data.history(period="max")
Ethereum_History = Bitcoin_Data.history(period="max")
Cardano_History = Cardano_Data.history(period="max")
Solana_History = Solana_Data.history(period="max")

#Accessing crypto data to use in dataframe
BTC = yfinance.download(Bitcoin, start="2022-08-11", end="2022-08-11")
ETH = yfinance.download(Ethereum, start="2022-08-11", end="2022-08-11")
ADA = yfinance.download(Cardano, start="2022-08-11", end="2022-08-11")
SOL = yfinance.download(Solana, start="2022-08-11", end="2022-08-11")

#Bitcoin Section
streamlit.write("Bitcoin (BTC)")
Bitcoin_image = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"))
#Displaying image
streamlit.image(Bitcoin_image)
#Displaying dataframe
streamlit.table(BTC)
#Line chart for technical analysis
streamlit.bar_chart(Bitcoin_History.Close)

#Ethereum Section
streamlit.write("Ethereum (ETH)")
Ethereum_image = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"))
#Displaying image
streamlit.image(Ethereum_image)
#Displaying dataframe
streamlit.table(ETH)
#Line chart for technical analysis
streamlit.bar_chart(Ethereum_History.Close)

#Cardano Section
streamlit.write("Cardano (ADA)")
Cardano_image = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png"))
#Displaying image
streamlit.image(Cardano_image)
#Displaying dataframe
streamlit.table(ADA)
#Line chart for technical analysis
streamlit.bar_chart(Cardano_History.Close)

#Cardano Section
streamlit.write("Solana (SOL)")
Solana_image = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png"))
#Displaying image
streamlit.image(Solana_image)
#Displaying dataframe
streamlit.table(SOL)
#Line chart for technical analysis
streamlit.bar_chart(Solana_History.Close)
