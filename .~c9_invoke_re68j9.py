from flask import Flask, render_template, request, redirect   
import os, pymongo

MONGO_URI="mongodb+srv://root:1234@cluster0-byoef.mongodb.net/test?retryWrites=true&w=majority"
MONGO_DB="mamarecipes"

app = Flask(__name__)

def get_connection():
    conn=pymongo.MongoClient(MONGO_URI)
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add-recipe")
def add_recipe():
    
    return render_template("submit.html")
    
@app.route("/add-recipe", methods=["POST"])
def confirm_add_recipe():
    conn=get_connection()
    
    username = request.form["username"]
    time = request.form["est-time"]
    recipe_name = request.form["recipe-name"]
    recipe_tag = request.form["recipe-tag"]
    ingredients = request.form["ingredients"]
    directions = request.form["directions"]
    
    if recipe_tag == "chinese":
        tagged = "chinese"
        
    elif recipe_tag == "indian":
        tagged = "indian"
        
    elif recipe_tag == "malay":
        tagged = "malay"
        
    else:
        tagged = "western"
        
    
    add_recipe = conn[MONGO_DB]["recipes"].insert({
        "username": username,
        "time": time,
        "recipe_name": recipe_name,
        "recipe_tag": tagged,
        "ingredients": ingredients,
        "directions": directions
    })
    
    return redirect ("/")

@app.route("/search")
def search():
    return render_template("search.html")
    
@app.route("/search", methods=["POST"])
def submit_search():
    
    conn = get_connection()
    
    search_term = request.form["search-term"]
    search_word = request.form["search-word"]
    
    if search_term == "username":
        search_by="username"
    elif search_term == "ingredients":
        search_by="ingredients"
    else:
        search_by="recipe_tag"
        
    search_recipes = conn[MONGO_DB]["recipes"].find({
        search_by:{"$regex":search_word, "$options":"i"}
    }).limit(10)
        
    
    return render_template("search.html", search_recipes=search_recipes)

@app.route("/edit/<item_id>")
def edit(item_id):
    
    conn = get_connection()
    Object = ("ObjectId" + (item_id))
    
    search_recipes = conn[MONGO_DB]["recipes"].find({
        "_id": 'ObjectId("5e451aec57c8c6a5e9defc1d")'
    })
    
    for e in search_recipes:
        
    
    return render_template("edit.html", search_recipes=search_recipes)

if __name__  == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
        