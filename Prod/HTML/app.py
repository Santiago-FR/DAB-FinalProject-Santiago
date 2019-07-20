from sqlalchemy import func
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


# app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/kidPlaces_db.sqlite"

db = SQLAlchemy(app)

# ROute to home page

@app.route("/")
def home():
        return render_template("index.html")
    
engine = create_engine("sqlite:///db/HISTORIC_SITES_ALL.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Histsites = Base.classes.Hsites
OntSites = Base.classes.Ontsites
OntParks = Base.classes.Ontparks


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/HISTORIC_SITES_ALL.sqlite"

dbo = SQLAlchemy(app)

# ROute to home page

@app.route("/histsites")
def historic():
   results = dbo.session.query(Histsites.Site_Name, Histsites.Site_type, Histsites.Site_dated, Histsites.Site_designated, Histsites.Site_location, Histsites.Site_coordinates , Histsites.Site_latitude, Histsites.Site_longitude, Histsites.Site_description).all()
   return jsonify(results)

@app.route("/parks")
def parks():
   results = dbo.session.query(OntParks.Park_Name ,OntParks.Latitude, OntParks.Longitude, OntParks.Type).all()
   return jsonify(results)

@app.route("/onsites")
def sites():
   results = dbo.session.query(OntSites.Business_Name, OntSites.Business_type, OntSites.City, OntSites.Country, OntSites.Address , OntSites.Zipcode ,OntSites.Latitude ,OntSites.Longitude, OntSites.url).all()
   return jsonify(results)

if __name__ == "__main__":
    app.run()
