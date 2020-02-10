from flask import Flask, render_template, request   
<<<<<<< HEAD
import os, pymongo

app = Flask(__name__)

MONGO_URI="mongodb+srv://root:1234@cluster0-byoef.mongodb.net/test?retryWrites=true&w=majority"
MONGO_DB="mamarecipes"

def get_connection():
    conn=pymongo.MongoClient(MONGO_URI)
    return conn

# paul --> mongo "mongodb+srv://cluster0-byoef.mongodb.net/test"  --username root

@app.route("/")
def index():
    conn = get_connection()
    call_data = conn[MONGO_DB]["Western"].find()
    
    # return render_template("index.html", call_data=call_data)
    return render_template("index.html", call_data=call_data)
    
=======
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

>>>>>>> 276f6af3a86ef3b30ca9d3b15555430d2c33ed47
if __name__  == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
        