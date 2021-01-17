from yahoo_fin import stock_info as si
import plotly.graph_objects as go
import os

ticker = ['SNDL', 'PSTH', 'TSLA', 'SQ', 'IPOE', 'AJAX', 'F']
names = ['David', 'Poles', 'Presley', 'Mark', 'Jack', 'Rex', 'Josh']
startPrice = [0.68, 27.75, 867.92, 241.99, 19.02, 11.52, 9.00]
currentPrice = []
percentReturn = []
for elem in range(0,len(ticker)):
    currentPrice.append(si.get_live_price(ticker[elem]))

for i in range(0, len(startPrice)):
    percentReturn.append(((currentPrice[i]-startPrice[i])/startPrice[i]))

max_index = percentReturn.index(max(percentReturn))

#save values into dictionary for easy access in html
myDict = {}
myDict["names"] = names
myDict["ticker"] = ticker
myDict["startPrice"] = startPrice
myDict["currentPrice"] = currentPrice
myDict["percentReturn"] = percentReturn
myDict["max"] = max_index

fig = go.Figure(data=[go.Table(
    header=dict(values=['Name','Ticker', 'Percent Return'],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
    cells=dict(values=[myDict["names"],ticker, # 1st column
                        percentReturn], # 2nd column
               line_color='darkslategray',
               fill_color='lightcyan',
               align='left'))
])

fig.update_layout(width=500, height=1000)
fig.write_image("plot.png")