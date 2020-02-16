from flask import Flask, render_template, request, redirect, url_for  
import os, pymongo
from bson.objectid import ObjectId

MONGO_URI="mongodb+srv://root:1234@cluster0-byoef.mongodb.net/test?retryWrites=true&w=majority"
MONGO_DB="mamarecipes"

app = Flask(__name__)

def get_connection():
    conn=pymongo.MongoClient(MONGO_URI)
    return conn
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recipes")
def recipes():
    
    return render_template("recipes.html")

if __name__  == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
        