from flask import Flask, render_template, redirect
from pymongo import MongoClient
import mission_to_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = MongoClient("mongodb://localhost:27017/marsscraped_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    collection = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=collection)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    collection = mongo.db.collection

    # Run the scrape function
    scrapeddata = mission_to_mars.marsscraping()

    # Update the Mongo database using update and upsert=True
    collection.update({}, scrapeddata, upsert=True)

    # Redirect back to home page
    return redirect("/", code = 302)


if __name__ == "__main__":
    app.run(debug=True)