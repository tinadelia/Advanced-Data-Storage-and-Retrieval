#Import of Dependencys
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)
# Flask Setup
app = Flask(__name__)
# Flask Routes
#   * Home page.
#   * List all routes that are available.
@app.route("/")
def route_avalible():
   """List all available api routes."""
   return (
       f"Available Routes:<br/>"
       f"/api/v1.0/precipitation<br/>"
       f"/api/v1.0/stations"
       f"/api/v1.0/tobs"
       f"/api/v1.0/<start>"
       f"/api/v1.0/<start>/<end>"
   )
# * /api/v1.0/precipitation
#   * Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
   """Return a Json of Precipitation Dates and actual precipitation"""
   # Convert the query results to a Dictionary using date as the key and prcp as the value.
   results = session.query(Measurement.date, Measurement.prcp).all()
   # Return the JSON representation of your dictionary.
   all_precipitation = []
   for date, prcp in results:
       precipitation_dict = {}
       precipitation_dict["date"] = date
       precipitation_dict["prcp"] = prcp
       all_precipitation.append(precipitation_dict)
   return jsonify(all_precipitation)
@app.route("/api/v1.0/stations")
def stations():
   """Return a list of JSON list of stations from the dataset."""
   # Return a JSON list of stations from the dataset.
   results = session.query(Station.name, Station.station).all()
   # Convert list of tuples into normal list
   all_stations = list(np.ravel(results))
   return jsonify(all_stations):