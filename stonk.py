from flask import Flask, render_template
import matplotlib.pyplot as plt
from yahoo_fin import stock_info as si
from decimal import Decimal


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def printrand():
    ticker = ['SNDL', 'PSTH', 'TSLA', 'SQ', 'IPOE', 'AJAX', 'F']
    names = ['David', 'Poles', 'Presley', 'Mark', 'Jack', 'Rex', 'Jawsh']
    startPrice = [0.68, 27.75, 867.92, 241.99, 19.02, 11.52, 9.00]
    currentPrice = []
    percentReturn = []
    for elem in range(0,len(ticker)):
        currentPrice.append(round(si.get_live_price(ticker[elem]),2))

    for i in range(0, len(startPrice)):
        percentReturn.append(round((((currentPrice[i]-startPrice[i])/startPrice[i])*100),2))

    max_index = percentReturn.index(max(percentReturn))

    #save values into dictionary for easy access in html
    myDict = {}
    myDict["names"] = names
    myDict["ticker"] = ticker
    myDict["startPrice"] = startPrice
    myDict["currentPrice"] = currentPrice
    myDict["percentReturn"] = percentReturn
    myDict["max"] = max_index
    myDict["test"] = {False, False, False, False, True, False, False}

    #test

    positive = []
    negative = []

    for i in range(0, len(names)):
        negative.append(percentReturn[i] < 0)
        positive.append(percentReturn[i] >= 0)
        # plt.bar(names[i][negative[i]], percentReturn[i][negative[i]], color = 'red')
        # plt.bar(names[i][positive[i]], percentReturn[i][positive[i]], color = 'green')


    for i in range(0, len(names)):
        plt.bar(names[i], percentReturn[i][positive[i]], color = 'forestgreen', edgecolor = 'blue', linewidth = 1.5)
        plt.bar(names[i], percentReturn[i][negative[i]], color = 'red', edgecolor = 'blue', linewidth = 1.5)
    
    plt.ylabel('% Returnz', fontsize = 14)
    plt.rc('axes', axisbelow=True)
    #plt.grid(False, color = 'gray', linestyle = 'dashed')
    plt.xlabel('Stonker', fontsize = 14)
    plt.title('Current Returns: Stonks Competition')
    plt.savefig('static/stonk_graph.png', facecolor='purple', edgecolor='none')
    return render_template('web.html', content= myDict)

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response
	

if __name__ == '__main__':
	#app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='192.168.0.2', debug= True)