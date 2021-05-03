
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config[MONGO_URI] = "mongodb://localhost:27017/mision_to_mars"
mongo = Pymongo(app)

@app.route("/")
def home ()
    mars_data = mongo.db.mars_database.find_one()
    return render_template('home.html', mars_data = mars_data)

@app.route("/scrappe")
def scrappe():
    mars_info = mongo
    mars_info
    mars_info

if __name__ == "__main__":
    app.run(debug=True)