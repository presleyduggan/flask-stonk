from flask import Flask, render_template
import matplotlib
matplotlib.use('Agg')
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Tahoma']
import matplotlib.pyplot as plt
from yahoo_fin import stock_info as si
from decimal import Decimal


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def stonk_showcase():
    myDict = {}

    myDict["names"] = ['David', 'Jack', 'Jawsh', 'Mark', 'Poles', 'Presley', 'Rex']
    myDict["ticker"] = ['SNDL', 'IPOE', 'F', 'SQ', 'PSTH', 'TSLA', 'AJAX']
    myDict["startPrice"] = [0.68, 19.02, 9.00, 241.99, 27.75, 867.92, 11.52]

    currentPrice = []
    percentReturn = []

    for elem in range(0,len(myDict["ticker"])):
        currentPrice.append(round(si.get_live_price(myDict["ticker"][elem]),2))

    for i in range(0, len(myDict["startPrice"])):
        percentReturn.append(round((((currentPrice[i]-myDict["startPrice"][i])/myDict["startPrice"][i])*100),2))

    max_index = percentReturn.index(max(percentReturn))
    #print(max_index)

    #save values into dictionary for easy access in html
    myDict["currentPrice"] = currentPrice
    myDict["percentReturn"] = percentReturn
    myDict["max"] = max_index

    positive = []
    negative = []

    for i in range(0, len(myDict["names"])):
        negative.append(percentReturn[i] < 0)
        positive.append(percentReturn[i] >= 0)


    for i in range(0, len(myDict["names"])):
        plt.bar(myDict["names"][i], percentReturn[i][positive[i]], color = 'forestgreen', edgecolor = 'blue', linewidth = 1.5)
        plt.bar(myDict["names"][i], percentReturn[i][negative[i]], color = 'red', edgecolor = 'blue', linewidth = 1.5)
    
    plt.ylabel('% Return', fontsize = 16, fontweight='bold')
    plt.rc('axes', axisbelow=True)
    #plt.grid(False, color = 'gray', linestyle = 'dashed')
    plt.xlabel('Stonker', fontsize = 16, fontweight='bold')
    plt.title('Current Returns', fontweight='bold', fontsize = 20)
    plt.savefig('static/stonk_graph.png', facecolor='blanchedalmond', edgecolor='none')
    return render_template('web.html', content= myDict)

# No caching at all for API endpoints.
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
	

if __name__ == '__main__':
	#app.run(host='127.0.0.1', port=8080, debug=True)
    #app.run(host='0.0.0.0', debug= True)
    app.run()