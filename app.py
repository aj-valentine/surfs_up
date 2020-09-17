# Import all of our dependencies 
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up the engine database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect our database into our classes 
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create variables to reference each table 
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create the session link from Python to SQLite 
session = Session(engine)

# To define our Flask app (all other routes should go after this one)
app = Flask(__name__)

# Define the welcome route (root of the flask)
@app.route("/")

# Add routing information for all other routes - create a function and return statement will have f-strings as reference to all other routes 
# Create function welcome and add precipitation, stations, tobs, and temp routes into return statement 
def welcome():
    test = (f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>" 
        f"/api/v1.0/temp/start/end")
    return (test)

# Create a new route for precipitation - make sure aligned to the left and convert dictionary into a json file
@app.route("/api/v1.0/precipitation")

# Create the precipitation function 
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Create a new route for stations 
@app.route("/api/v1.0/stations")

# Create the stations function 
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Create a new route for the stats 
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create the stats function 
def stats():
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), flafunc.max(Measurement.tobs)]
    
    if not end:
        results = session.query(*sel).\
        filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Create a new route for tobs
@app.route("/api/v1.0/tobs")

# Create the tobs function 
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# End the flask call
if __name__ == '__main__':
    app.run()