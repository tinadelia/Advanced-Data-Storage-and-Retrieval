#Import of Dependencys
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Create our session (link) from Python to the DB
session = Session(engine)


#precipitation data chart
precipitation_data = [	
   {"date": "prcp"},
   {"2010-01-01":	"0.08"},
   {"2010-01-02":	"0.00"},
   {"2010-01-03":	"0.00"},
   {"2010-01-04":	"0.00"},
   {"2010-01-06":	"NaN"},
   {"2010-01-07":	"0.06"},
   {"2010-01-08":	"0.00"},
   {"2010-01-09":	"0.00"},
   {"2010-01-10":	"0.00"},
   {"2010-01-11":	"0.01"}
   ]

#statiion data chart
station_data = [
{'Station Name': 'Counts'},
{'USC00519281': 2772},
{'USC00519397': 2724},
{'USC00513117': 2709},
{'USC00519523': 2669},
{'USC00516128': 2612},
{'USC00514830': 2202},
{'USC00511918': 1979},
{'USC00517948': 1372},
{'USC00518838': 511}
]


#tobs data chart
tobs_data = [
{'date': 'prcp'},
{'2016-08-24':	0.08},
{'2016-08-24':	2.15},
{'2016-08-24':	2.28},
{'2016-08-24':	'NaN'},
{'2016-08-24':	1.22},
{'2016-08-24':	2.15},
{'2016-08-24':	1.45},
{'2016-08-25':	0.08},
{'2016-08-25':	0.08},
{'2016-08-25':	0.00}
]

#start data chart
start_data= [
{"MinTemp" : 62.0},
{"AvgTemp": 69.57142857142857},
{"MaxTemp": 74.0}
]

#start/ end data chart
start_end_data= [
{"MinTemp" : 53.0},
{"AvgTemp": 73.43127438710152},
{"MaxTemp": 87.0}
]


# Flask Setup
app = Flask(__name__)


#List all routes that are available.
@app.route("/")
def available_routes():
   """List all available api routes."""
   return (
       f"Available Routes:<br/>"
       f"/api/v1.0/precipitation<br/>"
       f"/api/v1.0/stations<br/>"
       f"/api/v1.0/tobs<br/>"
       f"/api/v1.0/start<br/>"
       f"/api/v1.0/start/end"
   )


@app.route("/api/v1.0/precipitation")
def precipitation():
  
   return jsonify(precipitation_data)


@app.route("/api/v1.0/stations")
def stations():

   return jsonify(station_data)


@app.route("/api/v1.0/tobs")
def tobs():

   return jsonify(tobs_data)

@app.route("/api/v1.0/start")
def start():

   return jsonify(start_data)

@app.route("/api/v1.0/start/end")
def start_end():

   return jsonify(start_end_data)

if __name__ == '__main__':
   app.run(debug=True)

