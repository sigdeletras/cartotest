try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        if request.form['cartouser'] == None or request.form['cartotable'] == None:

            error = 'Invalid Credentials. Please try again.'

        else:

            cartouser = request.form['cartouser']
            cartotable = request.form['cartotable']
            cartourl = ("https://{}.carto.com/api/v1/sql?q=select%20*%20from%20{}%20order%20by%20cartodb_id".format(cartouser, cartotable))

            response = urlopen(cartourl)

            data = response.read().decode("utf-8")

            datarows = json.loads(data)
            
            return render_template('cartotableviewer.html', cartouser=cartouser, datarows = datarows)

    return render_template('cartotableviewer.html', error=error)

@app.errorhandler(500)
def page_not_found500(e):
    error = 'Invalid Credentials. Please try again'
    return render_template('cartotableviewer.html', error=error)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()