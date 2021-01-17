from flask import Flask, render_template
import matplotlib.pyplot as plt
from yahoo_fin import stock_info as si


app = Flask(__name__)
@app.route('/')
def printrand():
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

    #test

    graph = plt.bar(names, percentReturn)
    plt.ylabel('% Return', fontsize = 14)
    plt.xlabel('Stonker', fontsize = 14)
    plt.title('Current Returns: Stonks Competition')
    plt.savefig('static/stonk_graph.png')
    return render_template('web.html', content= max_index)
	

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)