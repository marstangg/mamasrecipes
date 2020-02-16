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
    
    conn = get_connection()
    
    recipes = conn[MONGO_DB]["recipes"].find({})

    return render_template("recipes.html", recipes=recipes)

@app.route("/add-recipe")
def add_recipe():
    
    return render_template("add-recipe.html")

@app.route("/add-recipe", methods=["POST"])
def submit_add_recipe():
    
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
    
    add_recipe = conn[MONGO_DB]["recipes"].insert_one({
        "username": username,
        "time": time,
        "recipe_name": recipe_name,
        "recipe_tag": tagged,
        "ingredients": ingredients,
        "directions": directions
    })
    
    return redirect("/")
    
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
    })
    
    
    return render_template("search.html", search_recipes=search_recipes)

@app.route("/edit/<recipe_id>")
def edit(recipe_id):
    
    conn = get_connection()
    
    search_recipes = conn[MONGO_DB]["recipes"].find_one({
        "_id": ObjectId(recipe_id)
    })
    
    return render_template("edit.html", recipe_id=recipe_id, search_recipes=search_recipes)
    
@app.route("/edit/<recipe_id>", methods=["POST"])
def submit_edit(recipe_id):
    
    return redirect("/recipes")
    
if __name__  == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
        