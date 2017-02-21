# Carto Table Viewer
Simple table viewer using the CartoDB SQL API. The web application is developed with [Flask](http://flask.pocoo.org/), a microframework for Python based on Werkzeug and Jinja 2.

##Usage 
- Visit the web [https://cartotableviewer.herokuapp.com/](https://cartotableviewer.herokuapp.com/)
- Enter your Carto username and a name of a dataset. (e.g. sigdeletras festival_patios_cordoba)
- Click 'Load Data'.

##Enviroment

Dependencies

Python (>= 3.5)

```
$ git clone https://github.com/sigdeletras/cartotest.git
$ cd cartotest
$ virtualenv venv
$ source venv/bin/activate
```

Please refer to pip requirements.txt for list of required modules
```
$ pip install -r requirements.txt
```

## Run local server ##

```
$ python app.py
```
