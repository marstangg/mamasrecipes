from flask import Flask, render_template, request   
import os

MONGO_URI="mongodb+srv://root:<1234>@cluster0-byoef.mongodb.net/test?retryWrites=true&w=majority"
MONGO_DB

def get_connection()

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

if __name__  == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
        