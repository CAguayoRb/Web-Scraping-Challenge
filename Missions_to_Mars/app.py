
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
    mars_mongo = mongo.db.mars_info
    mars_info = scrape_mars.scrape_mars_news()
    mars_info = scrape_mars.scrape_mars_facts()
    mars_info = scrape_mars.scrape_mars_hemispheres()
    mars_mongo.update({},mars_info,upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)